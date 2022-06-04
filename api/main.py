import sys
sys.dont_write_bytecode = True

from model import Event
from fastapi import FastAPI
from router import get_events
from router_sample import get_events_test
from starlette.requests import Request
from db import SessionLocal

app = FastAPI()

app.include_router(get_events.router)
app.include_router(get_events_test.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response