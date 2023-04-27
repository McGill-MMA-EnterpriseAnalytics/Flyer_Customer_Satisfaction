import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler


def log_transform(x):
    return np.log(x + 1)
def non_transform(x):
    return x

class DataProcessor:
    def __init__(self):
        pass

    @staticmethod
    def prep_training_data(data: pd.DataFrame):

        df = data[['Gender_Female', 'Customer Type_Loyal Customer',
                 'Type of Travel_Business',
                 'Type of Travel_Personal', 'Class_Business',
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
                 'satisfaction']]

        X_train = df[['Gender_Female', 'Customer Type_Loyal Customer',
                      'Type of Travel_Business',
                      'Type of Travel_Personal', 'Class_Business',
                      'Class_Eco', 'Age',
                      'Flight Distance', 'Departure Delay in Minutes',
                      'Arrival Delay in Minutes', 'Inflight wifi service',
                      'Departure/Arrival time convenient',
                      'Ease of Online booking', 'Gate location',
                      'Food and drink', 'Online boarding',
                      'Seat comfort', 'Inflight entertainment',
                      'On-board service', 'Leg room service',
                      'Baggage handling', 'Checkin service',
                      'Inflight service', 'Cleanliness', ]]
        y_train = df['satisfaction'].values

        return X_train, y_train

    def prep_inference_data(data: pd.DataFrame):

        df = data[['Gender_Female', 'Customer Type_Loyal Customer',
                 'Type of Travel_Business',
                 'Type of Travel_Personal', 'Class_Business',
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
                 ]]

        X_train = df[['Gender_Female', 'Customer Type_Loyal Customer',
                      'Type of Travel_Business',
                      'Type of Travel_Personal', 'Class_Business',
                      'Class_Eco', 'Age',
                      'Flight Distance', 'Departure Delay in Minutes',
                      'Arrival Delay in Minutes', 'Inflight wifi service',
                      'Departure/Arrival time convenient',
                      'Ease of Online booking', 'Gate location',
                      'Food and drink', 'Online boarding',
                      'Seat comfort', 'Inflight entertainment',
                      'On-board service', 'Leg room service',
                      'Baggage handling', 'Checkin service',
                      'Inflight service', 'Cleanliness', ]]

        return X_train

    @staticmethod
    def __handle_null__(data_df :pd.DataFrame):
        data_df_null = data_df[['Departure Delay in Minutes', 'Arrival Delay in Minutes']]
        imputer = IterativeImputer()
        imputed = imputer.fit_transform(data_df_null)
        data_df_cleaned = data_df.copy()
        data_df_cleaned.loc[:, ['Departure Delay in Minutes', 'Arrival Delay in Minutes']] = imputed
        return data_df_cleaned

    @staticmethod
    def __handle_outlier(data_df: pd.DataFrame, outlier_cols: [] ):
        if data_df is not None:
            X = data_df[outlier_cols]

            isolation_forest = IsolationForest(random_state=42, contamination=0.01)
            outlier_pred = isolation_forest.fit_predict(X)

            return data_df.iloc[outlier_pred == 1]

    @staticmethod
    def __normalize_imputation__(data_df : pd.DataFrame):
        categorical_cols = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
        target_col = ['satisfaction']
        satisfaction_cols = ['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking',
                             'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
                             'Inflight entertainment', 'On-board service', 'Leg room service',
                             'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness']

        log_pipeline = make_pipeline(
            #    SimpleImputer(strategy="median"),
            IterativeImputer(),
            FunctionTransformer(log_transform, feature_names_out="one-to-one"))

        iterative_impute_pipeline = make_pipeline(
            IterativeImputer(),
            FunctionTransformer(non_transform, feature_names_out="one-to-one"))

        cat_pipeline = make_pipeline(
            SimpleImputer(strategy="most_frequent"),
            OneHotEncoder(handle_unknown="ignore"))

        knn_impute_pipeline = make_pipeline(
            KNNImputer(missing_values=0, n_neighbors=5, weights='uniform', metric='nan_euclidean'))

        default_num_pipeline = make_pipeline(StandardScaler())

        normalize_preprocessing = ColumnTransformer([
            ("log", log_pipeline, ['Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']),
            ("cat", cat_pipeline, categorical_cols),
            ("std", default_num_pipeline, ['Age']),
            ("score", knn_impute_pipeline, satisfaction_cols)
        ],
            remainder='passthrough',
            verbose_feature_names_out=False
        )

        imputing_preprocessing = ColumnTransformer([
            ("iter", iterative_impute_pipeline, ['Departure Delay in Minutes', 'Arrival Delay in Minutes']),
            ("cat", cat_pipeline, categorical_cols),
            ("score", knn_impute_pipeline, satisfaction_cols)
        ],
            remainder='passthrough',
            verbose_feature_names_out=False
        )

        airplane_train = data_df.copy()
        airplane_train = imputing_preprocessing.fit_transform(airplane_train)
        airplane_train = pd.DataFrame(airplane_train,
                                      columns=imputing_preprocessing.get_feature_names_out(),
                                      index=data_df.index)
        airplane_train.drop(columns=['User_id'], inplace=True)

        airplane_train_normalized = normalize_preprocessing.fit_transform(data_df)
        airplane_train_normalized = pd.DataFrame(airplane_train_normalized,
                                                 columns=normalize_preprocessing.get_feature_names_out(),
                                                 index=data_df.index)
        airplane_train_normalized.drop(columns=['User_id'], inplace=True)

        return airplane_train_normalized, airplane_train

    @staticmethod
    def clean_data(data_df :pd.DataFrame, is_train: False):
        data_df_normalized = None
        data_df_imputed = None
        if data_df is not None and is_train:
            data_df_cleaned = DataProcessor.__handle_null__(data_df)

            outlier_cols = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
            data_df_cleaned = DataProcessor.__handle_outlier(data_df_cleaned, outlier_cols)

            data_df_normalized, data_df_imputed = DataProcessor.__normalize_imputation__(data_df_cleaned)

        else:
            data_df_normalized, data_df_imputed = DataProcessor.__normalize_imputation__(data_df)

        return data_df_normalized, data_df_imputed

