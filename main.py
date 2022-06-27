from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello! This is my first API"

@app.get("/blogs/")
def blogs(limit: int = 10, published: bool = True, sort: Optional[str] = "latest"):
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} unpublished blogs"}


@app.get("/blogs/unpublished")
def unpublished():
    return {'data': 'unpublished blogs'}

@app.get("/blogs/{id}")
def about(id: int):
    #fetch blog with id 
    return {'data':id}