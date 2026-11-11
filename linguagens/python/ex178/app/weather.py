import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10

# Códigos WMO usados pela Open-Meteo
WEATHER_CODES = {
    0: "Céu limpo",
    1: "Principalmente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Neblina",
    48: "Neblina com geada",
    51: "Garoa leve",
    53: "Garoa moderada",
    55: "Garoa intensa",
    56: "Garoa congelante leve",
    57: "Garoa congelante intensa",
    61: "Chuva leve",
    63: "Chuva moderada",
    65: "Chuva forte",
    66: "Chuva congelante leve",
    67: "Chuva congelante intensa",
    71: "Neve leve",
    73: "Neve moderada",
    75: "Neve forte",
    77: "Grãos de neve",
    80: "Pancadas de chuva leves",
    81: "Pancadas de chuva moderadas",
    82: "Pancadas de chuva fortes",
    85: "Pancadas de neve leves",
    86: "Pancadas de neve fortes",
    95: "Tempestade",
    96: "Tempestade com granizo leve",
    99: "Tempestade com granizo forte",
}


class CityNotFoundError(Exception):
    pass


def describe_weather(code):
    return WEATHER_CODES.get(code, "Condição desconhecida")


def geocode_city(city: str):
    response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1,
            "language": "pt",
            "format": "json",
        },
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    results = response.json().get("results") or []

    if not results:
        raise CityNotFoundError(f"Cidade não encontrada: {city}")

    return results[0]


def fetch_weather(city: str):

    city = city.strip()

    if not city:
        raise CityNotFoundError("Cidade não informada")

    location = geocode_city(city)

    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": (
                "temperature_2m,relative_humidity_2m,apparent_temperature,"
                "precipitation,weather_code,wind_speed_10m"
            ),
            "timezone": "auto",
        },
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    data = response.json()
    current = data.get("current") or {}

    if not current:
        raise RuntimeError("Resposta inválida do serviço meteorológico")

    return {
        "city": location.get("name") or city,
        "country": location.get("country"),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": data.get("timezone"),
        "current": {
            "time": current.get("time"),
            "temperature_c": current.get("temperature_2m"),
            "apparent_temperature_c": current.get("apparent_temperature"),
            "humidity_percent": current.get("relative_humidity_2m"),
            "precipitation_mm": current.get("precipitation"),
            "wind_speed_kmh": current.get("wind_speed_10m"),
            "weather_code": current.get("weather_code"),
            "conditions": describe_weather(current.get("weather_code")),
        },
    }
