
from fastapi import FastAPI, HTTPException
from requests.exceptions import RequestException
import redis
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
import requests
from app.weather import fetch_weather, CityNotFoundError
from app.cache import (
    get_cached_weather,
    set_cached_weather
)

from fastapi import Request

limiter = Limiter(
    key_func=get_remote_address
)

app = FastAPI(
    title="Weather API",
    description="API de consulta meteorológica",
    version="1.0.0"
)

app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)


@app.get("/")

def home():
    return {
        "message": "Weather API funcionando!"
    }


@app.get("/weather")
@limiter.limit("10/minute")
def get_weather(request: Request, city: str):

    try:
        # 1. Verificar o cache
        cached_data = get_cached_weather(city)

        if cached_data:
            return {
                "source": "cache",
                "data": cached_data
            }

        # 2. Consultar a API externa
        weather_data = fetch_weather(city)

        # 3. Armazenar o resultado
        set_cached_weather(city, weather_data)

        # 4. Retornar os dados
        return {
            "source": "external_api",
            "data": weather_data
        }

    except CityNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Tempo limite da consulta meteorológica excedido"
        )

    except RequestException:
        raise HTTPException(
            status_code=502,
            detail="Erro ao consultar o serviço meteorológico"
        )

    except redis.RedisError:
        raise HTTPException(
            status_code=503,
            detail="Serviço de cache indisponível"
        )

    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )