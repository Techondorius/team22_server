from router import get_events, edit_events, utils
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
import sys
sys.dont_write_bytecode = True


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def request_validation_handler(req, exc):
    return JSONResponse(status_code=400, content={"code": "InvalidParameter"})

app.include_router(get_events.router)
app.include_router(edit_events.router)
app.include_router(utils.router)
