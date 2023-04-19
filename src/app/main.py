import uvicorn
from typing import Union
from fastapi import FastAPI, APIRouter, Query, Response
import src.app.controller.controller as c
import requests
import pandas as pd
from http import HTTPStatus as sc
import logging


logger = logging.getLogger(__name__)
app = FastAPI() #openapi_url="/openapi.json"


api_router = APIRouter()
api_router.include_router(c.api_router, prefix="/processor/controller", tags=[],include_in_schema=True)
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hey"}


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port="6060")
