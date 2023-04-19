import requests
import pandas as pd
from http import HTTPStatus as req_status
import json
from json import JSONEncoder
import datetime


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


class DataExtractProcessor:
    def __init__(self):
        pass


    @staticmethod
    def get_data_from_api(request_url: str, params: dict = None):
        if len(request_url) > 0:
            try:
                response = requests.get(request_url, params=params, verify=False)
                data = ""

                if response.status_code == req_status.OK:
                    content_type = response.headers['content-type'].split(';')[0]
                    if content_type == "application/json":
                        data = response.json()
                return pd.DataFrame.from_dict(data)
            except RuntimeError as ex:
                print(ex)
        else:
            raise ValueError("Url is invalid or empty")


    @staticmethod
    def save_results(request_url: str, result, params: dict = None):
        if isinstance(result, pd.DataFrame):
            result = json.loads(result.to_json(orient="records"))

        response = requests.post(url=request_url, params=params, json=result, verify=False)

        if response.status_code == req_status.OK:
            print("ok")

    @staticmethod
    def get_training_data(request_url: str, params: dict = None):
        return DataExtractProcessor.get_data_from_api(request_url, params= params)


    @staticmethod
    def get_inference_data(request_url: str, params: dict = None):
        return DataExtractProcessor.get_data_from_api(request_url, params= params)
