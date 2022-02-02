import pandas as pd
import redis
import json

redis_host = "localhost"
redis_port = 6379


def redis_string():
    try:
        with open('data.json') as files:
            json_obj = json.load(files)
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("test", json.dumps(json_obj))
        name = r.get("test")
        print(name)
    except Exception as err:
        print(err)

redis_string()

