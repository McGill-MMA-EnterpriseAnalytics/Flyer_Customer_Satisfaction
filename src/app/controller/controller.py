from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel
from src.app.model_lib.preprocessor import  ModelProcessor as mp
import logging
import json

logger = logging.getLogger(__name__)

api_router = APIRouter()

@api_router.post("/process/model", status_code=200, response_model=object)
def process_model():
    a = mp.process_model(None)
    return "Ok"