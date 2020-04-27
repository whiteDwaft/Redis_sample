from fastapi import FastAPI
from starlette.requests import Request
import requests
import redis
import datetime

i = 0;
r = redis.Redis(host='yourhost', port='yourport')
app = FastAPI()

@app.get("/")
async def my_route(request: Request) :
    url = request.url.path
    update(url,"Hello World")
    return {"message": "Hello World"}

def update(url,message):
    r.hset("log","request", url)
    r.hset("log","time",str(datetime.datetime.today()))
    r.hset("log","message",message)
    print(r.hgetall("log"))

if __name__ == '__main__':
    for i in range(10):
        requests.get("http://127.0.0.1:8000/")