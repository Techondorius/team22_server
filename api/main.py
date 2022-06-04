from pydantic import ValidationError
from model import Event
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from router import get_events, edit_events

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def request_validation_handler(req, exc):
    return JSONResponse(status_code=400, content={"code": "InvalidParameter"})

app.include_router(get_events.router)
app.include_router(edit_events.router)
