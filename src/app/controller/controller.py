import pandas as pd
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel
from src.app.model_lib.model_processor import ModelProcessor as mp
from src.app.model_lib.preprocessor import DataProcessor as d_proc
from src.app.model_lib.data_extract_processor import DataExtractProcessor as dcp
from src.app.model_lib import raw_file_loader as rld
from src.app.model_lib.EnumFileType import EnumFileType
import logging
import json
from pydantic import parse_obj_as
from fastapi.encoders import jsonable_encoder
from datetime import datetime


class input_model(BaseModel):
    TravelType: str | None = None
    InFlightService: int
    Gender: str
    Customer_Type: int
    Travel_Type: str
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
def process_model_train():
    result = mp.train_model(save_model=True)
    return result


@api_router.post("/model/infer_adhoc", status_code=200, response_model=object)
def process_model_infer_adhoc(item: list[input_model]):
    column_map = {
    }

    infer_data_df = pd.DataFrame(jsonable_encoder(item))  # pd.read_json(item.dict())
    infer_data_df = infer_data_df.rename(columns=column_map)
    result = mp.predict_results(infer_data_df=infer_data_df, save_result=False)
    return result


@api_router.post("/model/infer", status_code=200, response_model=object)
def process_model_infer():
    result = mp.predict_results(infer_data_df=None, save_result=True)
    return result


@api_router.post("/dataPrep/ImportTrainData", status_code=200, response_model=object)
def import_train_data():
    loader = rld.RawFileLoader()
    loader.process("../app/data", "airline_train_raw.csv", EnumFileType.TRAIN)
    return "Ok"
    # seq_pc.SequenceProcessor.save_results(results)


@api_router.post("/dataPrep/ImportTestData", status_code=200, response_model=object)
def import_test_data():
    loader = rld.RawFileLoader()
    loader.process("../app/data", "airline_test_raw.csv", EnumFileType.TEST)
    return "Ok"
    # seq_pc.SequenceProcessor.save_results(results)


@api_router.post("/dataPrep/CleanData", status_code=200, response_model=object)
def process_clean_data():
    columnNameMap = {
        "User_id": "User_id",
        "Gender": "Gender",
        "CustomerType": "Customer Type",
        "Age": "Age",
        "TravelType": "Type of Travel",
        "Class": "Class",
        "Distance": "Flight Distance",
        "InflightWifi": "Inflight wifi service",
        "DeptArriveConvenience": "Departure/Arrival time convenient",
        "OnlineBooking": "Ease of Online booking",
        "GateLocation": "Gate location",
        "Food": "Food and drink",
        "OnlineBoarding": "Online boarding",
        "SeatComfort": "Seat comfort",
        "InflightEntertainment": "Inflight entertainment",
        "OnboardService": "On-board service",
        "LegRoom": "Leg room service",
        "Baggage": "Baggage handling",
        "Checkin": "Checkin service",
        "InflightService": "Inflight service",
        "Cleanliness": "Cleanliness",
        "DepartDelay": "Departure Delay in Minutes",
        "ArriveDelay": "Arrival Delay in Minutes",
        "Satisfaction": "satisfaction",
        "DataDate": "DataDate",
    }

    payloadColnameMap = {
        "Departure Delay in Minutes": "DepartDelay",
        "Arrival Delay in Minutes": "ArriveDelay",
        "Customer Type_Loyal Customer": "CustomerType_Loyal",
        "Customer Type_disloyal Customer": "CustomerType_Disloyal",
        "Gender_Female": "Gender_Female",
        "Gender_Male": "Gender_Male",
        "Type of Travel_Business travel": "TravelType_Business",
        "Inflight wifi service": "InflightWifi",
        "Departure/Arrival time convenient": "DeptArriveConvenience",
        "Ease of Online booking": "OnlineBooking",
        "Gate location": "GateLocation",
        "Food and drink": "Food",
        "Online boarding": "OnlineBoarding",
        "Seat comfort": "SeatComfort",
        "Inflight entertainment": "InflightEntertainment",
        "On-board service": "OnboardService",
        "Leg room service": "LegRoom",
        "Baggage handling": "Baggage",
        "Checkin service": "Checkin",
        "Inflight service": "InflightService",
        "Cleanliness": "Cleanliness",
        "AirlineDataID": "AirlineDataID",
        "Flight Distance": "Distance",
        "Age": "Age",
        "satisfaction": "Satisfaction",
        "DataDate": "DataDate",
        "IsTrain": "IsTrain"
    }

    columnTypeMap = {
        "Gender_Female": int,
        "Gender_Male": int,
        "CustomerType_Loyal": int,
        "CustomerType_Disloyal": int,
        "Age": int,
        "Distance": int,
        "InflightWifi": int,
        "DeptArriveConvenience": int,
        "OnlineBooking": int,
        "GateLocation": int,
        "Food": int,
        "OnlineBoarding": int,
        "SeatComfort": int,
        "InflightEntertainment": int,
        "OnboardService": int,
        "LegRoom": int,
        "Baggage": int,
        "Checkin": int,
        "InflightService": int,
        "Cleanliness": int,
        "DepartDelay": int,
        "ArriveDelay": int,
        "Satisfaction": str,
        "DataDate": str,
        "TravelType_Business": int,
        "TravelType_Personal": int,
        "Class_Business" : int,
        "Class_Eco": int
    }

    train_url = "https://localhost:7118/api/etl/AirlineData/GetAirlineData?isTrain=true"
    train_data_df = dcp.get_training_data(train_url)
    train_data_df = train_data_df.rename(columns=columnNameMap)
    train_norm, train_imp = d_proc.clean_data(train_data_df, is_train=True)

    dateFormat = "%Y-%m-%dT%H:%M:%S"
    runDate = datetime.now().strftime(dateFormat)

    test_url = "https://localhost:7118/api/etl/AirlineData/GetAirlineData?isTrain=false"
    test_data_df = dcp.get_training_data(test_url)
    test_data_df = test_data_df.rename(columns=columnNameMap)
    test_norm, test_imp = d_proc.clean_data(test_data_df, is_train=False)

    data = pd.concat([train_imp, test_imp], ignore_index=True)
    data.rename(columns=payloadColnameMap, inplace=True)
    data.fillna(0, inplace=True)
    for col in columnTypeMap.keys():
        if col in data.columns:
            data[col] = data[col].astype(columnTypeMap[col])

    dcp.save_results(
        f"https://localhost:7118/api/etl/ModelData/SaveCleanModelInput?deleteExisting=true&rundate={runDate}",
        data)

    return "Ok"
    # seq_pc.SequenceProcessor.save_results(results)
