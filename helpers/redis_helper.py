import redis
import json

class RedisHelper:

    def __init__(self):
        with open('./config.json', 'r') as configJson:
            self.config = json.load(configJson)
        self.client = redis.Redis(host=self.config["redis"]["host"],
                                  port=self.config["redis"]["port"])

    def setData(self, key, value):
        self.client.set(key, value)

    def setDataWithExp(self, key, value, ttl):
        self.client.set(key, value, ex=ttl)

    def getData(self, key):
        return self.client.get(key)
    
    def getExpiration(self, key):
        return self.client.ttl(key)