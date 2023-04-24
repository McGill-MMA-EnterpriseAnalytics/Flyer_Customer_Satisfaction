import pandas as pd
from src.app.model_lib.data_extract_processor import DataExtractProcessor as dcp
from src.app.model_lib.preprocessor import DataProcessor as dp
import xgboost as xgb
from xgboost import cv, XGBClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from datetime import datetime


class ModelProcessor:
    def __init__(self):
        pass

    @staticmethod
    def train_model(save_model = True):
        use_api = False
        file_path ="../app/pickle/"
        data_path = "../../Data"
        url = ""

        if use_api:
            columnMap = {

            }
            train_data_df = dcp.get_training_data(url)
            train_data_df = train_data_df.rename(columns=columnMap)
        else:
            train_data_df = pd.read_csv(data_path + "/airplane_train_processed_date.csv")

        X_train, y_train = dp.prep_training_data(train_data_df)

        params = {
            'objective': 'binary:logistic',
            'max_depth': 21,
            'alpha': 10,
            'learning_rate': 1.0,
            'n_estimators': 100
        }

        # instantiate the classifier
        xgb_clf = XGBClassifier(**params)
        le = LabelEncoder()

        y_ = le.fit_transform(y_train)
        xgb_clf.fit(X_train, y_)
        print(f"Model params: {xgb_clf}")

        if save_model:
            joblib.dump(xgb_clf, file_path + "final_classifier.pkl")
            print("Classification model Saved to", file_path)
            joblib.dump(le, file_path + "encoder.pkl")
            print("Label encoder Saved to", file_path)

        return "Ok"

    @staticmethod
    def predict_results(infer_data_df: pd.DataFrame, save_result=True):
        use_api = False
        file_path = "../app/pickle/"
        url = ""

        if infer_data_df is None or len(infer_data_df) <= 0:
            columnMap = {

            }

            infer_data_df = dcp.get_inference_data(url)
            infer_data_df = infer_data_df.rename(columns= columnMap)

        xgb_clf = joblib.load(file_path + "final_classifier.pkl")
        le = joblib.load(file_path + "encoder.pkl")
        X_test = dp.prep_inference_data(infer_data_df)

        y_pred = xgb_clf.predict(X_test)
        dateFormat = "%Y-%m-%dT%H:%M:%S"
        runDate = datetime.now().strftime(dateFormat)

        if save_result:
            if use_api:
                url = f"https://localhost:7118/api/model/ModelDataProcessed/SavePredictions?deleteExisting=False&runDate={runDate}"
                dcp.save_results(request_url=url, result=y_pred)
            else:
                y_pred.to_csv(file_path + "pip_prediction_result.csv")
                print("Prediction Result Saved to", file_path + "pip_prediction_result.csv")

        return y_pred
