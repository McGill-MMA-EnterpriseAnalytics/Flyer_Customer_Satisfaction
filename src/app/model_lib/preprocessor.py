import pandas as pd


class DataProcessor:
    def __init__(self):
        pass

    @staticmethod
    def prep_training_data(data: pd.DataFrame):

        df = data[['Gender_Female', 'Customer Type_Loyal Customer',
                 'Type of Travel_Business travel',
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
                 'satisfaction']]

        X_train = df[['Gender_Female', 'Customer Type_Loyal Customer',
                      'Type of Travel_Business travel',
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
                      'Inflight service', 'Cleanliness', ]]
        y_train = df['satisfaction'].values

        return X_train, y_train

    def prep_inference_data(data: pd.DataFrame):

        df = data[['Gender_Female', 'Customer Type_Loyal Customer',
                 'Type of Travel_Business travel',
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
                 ]]

        X_train = df[['Gender_Female', 'Customer Type_Loyal Customer',
                      'Type of Travel_Business travel',
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
                      'Inflight service', 'Cleanliness', ]]

        return X_train
