import uuid
import redis
from typing import Union
from typing import Callable

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Callable = None):
        value = self.redia_client.get(key)
        if value is not None:
            return fn(value) if fn else value

    def get_str(self, key):
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, fn=int)
