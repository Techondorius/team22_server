from model import Event
from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
def index():
    return 'Hello World'
