from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    date: datetime = None

@app.get('/hello')
async def say_hello():
    return {'message': 'Hello, World!'}

@app.post('/post')
async def post_data(post: Post):
    return post

