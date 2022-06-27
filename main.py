import imp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello! This is my first API"