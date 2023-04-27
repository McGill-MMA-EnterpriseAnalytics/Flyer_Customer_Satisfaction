import datetime
import numpy as np

import pandas as pd
from src.app.model_lib import db_handler as db
import os

from src.app.model_lib.EnumFileType import EnumFileType
from src.app.model_lib.EnumDatabase import EnumDatabase


class RawDataProcessor:
    columnNameMap = {
        "id": "User_id",
        "Gender": "Gender",
        "Customer Type": "CustomerType",
        "Age": "Age",
        "Type of Travel": "TravelType",
        "Class": "Class",
        "Flight Distance": "Distance",
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
        "Departure Delay in Minutes": "DepartDelay",
        "Arrival Delay in Minutes": "ArriveDelay",
        "satisfaction": "Satisfaction",
        "Date": "DataDate",
    }

    columnTypeMap = {
        "User_id": int,
        "Gender": str,
        "CustomerType": str,
        "Age": int,
        "TravelType": str,
        "Class": str,
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
    }

    def __init__(self):
        print('Raw File Processor Initialized')
        pass

    @staticmethod
    def get_from_file(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found")
        print("Reading raw data from file")

        data = pd.DataFrame()
        try:
            fileExt = os.path.splitext(file_path)[-1].lower()
            match fileExt:
                case '.csv':
                    data = pd.read_csv(file_path, dtype='string')
                case '.xls' | '.xlsx' | '.xlsm':
                    data = pd.read_excel(file_path, sheet_name=None, dtype='string')
        except Exception as ex:
            raise RuntimeError("Unable to retrieve files" + ex.__str__())

        return data

    def process(self, raw_data_df, file_type, root_dir: str = ""):
        root_dir = os.path.join(root_dir, "processed")
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)

        match file_type:
            case EnumFileType.TEST:
                print('Processing Test Data')
                self.__process_testData__(raw_data_df, root_dir)
            case EnumFileType.TRAIN:
                print('Processing Train Data')
                self.__process_trainData__(raw_data_df, root_dir)
            case _:
                print('None')

    def __process_testData__(self, raw_data: pd.DataFrame, root_dir: str) -> None:
        raw_data_df = raw_data.rename(columns=self.columnNameMap)

        raw_data_df['ArriveDelay'] = raw_data_df.ArriveDelay.fillna("0.0").astype(float).astype(int)
        raw_data_df = raw_data_df.astype(self.columnTypeMap)

        col_to_drop = []
        for col in list(raw_data_df.columns):
            if col not in self.columnNameMap.values():
                col_to_drop.append(col)

        raw_data_df.drop(columns=col_to_drop, inplace=True)

        handler = db.db_handler(EnumDatabase.SQL_SERVER)
        conn = handler.connect_db(server_name="LAPTOP-HMF8Q5ET\SQLEXPRESS",
                                  db_name="Enterprise")
        raw_data_df['IsTrain'] = 0
        #raw_data_df.reset_index(inplace=True)
        #raw_data_df.rename(columns={"index": "ID"}, inplace=True)
        #raw_data_df.ID = raw_data_df.ID + 1
        handler.write_to_db(conn, "dbo", "airline_raw", raw_data_df)

    def __process_trainData__(self, raw_data: pd.DataFrame, root_dir: str) -> None:
        raw_data_df = raw_data.rename(columns=self.columnNameMap)

        raw_data_df['ArriveDelay'] = raw_data_df.ArriveDelay.fillna("0.0").astype(float).astype(int)
        raw_data_df = raw_data_df.astype(self.columnTypeMap)

        col_to_drop = []
        for col in list(raw_data_df.columns):
            if col not in self.columnNameMap.values():
                col_to_drop.append(col)

        raw_data_df.drop(columns=col_to_drop, inplace=True)

        handler = db.db_handler(EnumDatabase.SQL_SERVER)
        conn = handler.connect_db(server_name="LAPTOP-HMF8Q5ET\SQLEXPRESS",
                                  db_name="Enterprise")
        raw_data_df['IsTrain'] = 1
        #raw_data_df.reset_index(inplace=True)
        #raw_data_df.rename(columns={"index": "ID"}, inplace=True)
        #raw_data_df.ID = raw_data_df.ID + 1
        handler.write_to_db(conn, "dbo", "airline_raw", raw_data_df)
