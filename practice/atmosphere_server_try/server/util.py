import pickle
import json
import numpy as np

__model = None
__data_columns = None


def get_predicted_land_type(air_temp, humidity):
    if air_temp < -10 or air_temp > 50:  # Example reasonable range
        return 'Invalid air temperature value'
    if humidity < 0 or humidity > 100:
        return 'Invalid humidity value'

    # Prepare the input for the model
    x = np.array([air_temp, humidity]).reshape(1, -1)

    # Predict the land type directly from the model output
    predicted_index = __model.predict(x)[0]  # This should return the land type as a string directly

    return predicted_index  # Return the predicted land type directly


def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/atmosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    print("Loading saved artifacts... done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_predicted_land_type(30, 40))  # Test prediction
