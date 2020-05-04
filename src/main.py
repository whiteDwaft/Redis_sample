from fastapi import FastAPI
from starlette.requests import Request
import requests
import redis
import datetime

i = 0;
r = redis.Redis(host='192.168.1.65', port='8080')
app = FastAPI()

@app.get("/")
async def my_route() :
    update("Hello World")
    return {"message": "goodbye World"}

def update(message):
    r.hset("log","time",str(datetime.datetime.today()))
    r.hset("log","message",message)
    print(r.hgetall("log"))

#if __name__ == '__main__':
#    for i in range(10):
 #       requests.get("http://127.0.0.1:8000/")