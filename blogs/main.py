from fastapi import FastAPI
from blogs.schemas import Blog


app = FastAPI()

@app.post("/blog")
def create(request: Blog):
    return request