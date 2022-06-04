from model import Event
from fastapi import FastAPI
from router import get_events

app = FastAPI()

app.include_router(get_events.router)
