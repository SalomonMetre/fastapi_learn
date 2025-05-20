from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    date: datetime = Field(default_factory=datetime.now())  # set current time by default

@app.get('/hello')
async def say_hello():
    return {"message": "Hello, World!"}

@app.post('/post')
async def post_data(post: Post):
    return post