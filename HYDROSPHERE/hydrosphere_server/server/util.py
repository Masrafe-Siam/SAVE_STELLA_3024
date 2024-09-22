import pickle
import json
import numpy as np
import pandas as pd

__model = None
__data_columns = None


def predict_plant_type(Dissolved_Oxygen, Temperature, pH):
    if not (1.0 <= Dissolved_Oxygen <= 15.0):
        return 'Invalid Dissolved Oxygen value. Must be between 1 and 15 mg/L.'
    if not (5 <= Temperature <= 30):
        return 'Invalid Temperature value. Must be between 5°C and 30°C.'
    if not (4.0 <= pH <= 9.5):
        return 'Invalid pH value. Must be between 4.0 and 9.5.'

    # Prepare the input for the model as a DataFrame
    input_data = pd.DataFrame([[Dissolved_Oxygen, Temperature, pH]], columns=['Dissolved_Oxygen', 'Temperature', 'pH'])

    predicted_index = __model.predict(input_data)[0]

    # Check if predicted_index is valid
    if 0 <= predicted_index < len(__data_columns):
        return __data_columns[predicted_index]  # Return the plant type
    else:
        return 'Prediction index out of range.'


def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/hydrosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts... done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(predict_plant_type(7, 25, 5))  # Test prediction
