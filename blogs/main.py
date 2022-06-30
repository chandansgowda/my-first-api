from fastapi import FastAPI
from blogs.schemas import Blog
from .database import engine
from . import schemas, models

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.post("/blog")
def create(request: Blog):
    return request