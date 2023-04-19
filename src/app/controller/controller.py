import pandas as pd
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel
from src.app.model_lib.model_processor import  ModelProcessor as mp
import logging
import json
from pydantic import parse_obj_as
from fastapi.encoders import jsonable_encoder

class input_model(BaseModel):
    TravelType: str | None = None
    InFlightService : int
    Gender : str
    Customer_Type: int
    Travel_Type : str
    '''
    'Type of Travel_Personal Travel', 'Class_Business',
    'Class_Eco', 'Age',
    'Flight Distance', 'Departure Delay in Minutes',
    'Arrival Delay in Minutes', 'Inflight wifi service',
    'Departure/Arrival time convenient',
    'Ease of Online booking', 'Gate location',
    'Food and drink', 'Online boarding',
    'Seat comfort', 'Inflight entertainment',
    'On-board service', 'Leg room service',
    'Baggage handling', 'Checkin service',
    'Inflight service', 'Cleanliness',

    '''

logger = logging.getLogger(__name__)

api_router = APIRouter()

@api_router.post("/model/train", status_code=200, response_model=object)
def process_model():
    result = mp.train_model(save_model=True)
    return result


@api_router.post("/model/infer_adhoc", status_code=200, response_model=object)
def process_model(item: list[input_model]):
    column_map = {
    }

    infer_data_df =  pd.DataFrame(jsonable_encoder(item))  #pd.read_json(item.dict())
    infer_data_df = infer_data_df.rename(columns=column_map)
    result = mp.predict_results(infer_data_df= infer_data_df, save_result=False)
    return result


@api_router.post("/model/infer", status_code=200, response_model=object)
def process_model():
    result = mp.predict_results(infer_data_df=None, save_result=False)
    return result

