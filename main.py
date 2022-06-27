from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello! This is my first API"

@app.get("/blogs/unpublished")
def unpublished():
    return {'data': 'unpublished blogs'}

@app.get("/blogs/{id}")
def about(id: int):
    #fetch blog with id 
    return {'data':id}