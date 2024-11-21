# small-service-1/app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello from Small Service 1"}
