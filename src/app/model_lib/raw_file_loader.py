#!pip install openpyxl

import os
from src.app.model_lib.EnumFileType import EnumFileType
from src.app.model_lib.db_handler import db_handler as db

from src.app.model_lib import raw_processor as r_proc


class RawFileLoader:
    __base_path__ = ".."
    __file_name__ = 'RawData_McGillMMA_20221014.xlsm'

    def __init__(self):
        print("File loader initalized")

    def process(self, base_path: str, file_name: str, fileType: EnumFileType):
        self.__base_path__ = ".." if base_path is None or base_path == "" else base_path
        self.__file_name__ = 'RawData_McGillMMA_20221014.xlsm' if file_name is None or file_name == "" else file_name

        raw_processor = r_proc.RawDataProcessor()
        #data = raw_processor.get_from_file(file_path=os.path.join(base_path, file_name))
        data = raw_processor.get_from_file(file_path=f"{base_path}/{file_name}")

        raw_processor.process(raw_data_df=data, file_type=fileType)