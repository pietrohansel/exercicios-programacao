
import os
import json
import redis

from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    decode_responses=True
)


def get_cached_weather(city: str):

    cached_data = redis_client.get(city.strip().lower())

    if cached_data:
        return json.loads(cached_data)

    return None


def set_cached_weather(city: str, data: dict):

    redis_client.set(
        city.strip().lower(),
        json.dumps(data),
        ex=43200 #12 horas
    )
