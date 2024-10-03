import pickle
import json
import numpy as np

__model = None
__data_columns = None

def get_predicted_plant_type(soil_temp, soil_ph):
    if soil_temp < 0 or soil_temp > 50:
        return 'Invalid soil temperature value'
    if soil_ph < 0 or soil_ph > 14:
        return 'Invalid soil pH value'

    # Prepare the input for the model
    x = np.array([soil_temp, soil_ph]).reshape(1, -1)
    return __model.predict(x)[0]  # Fixed to predict properly

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
    global __model
    if __model is None:
        with open('./artifacts/pedosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts... done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_predicted_plant_type(25, 6.5))  # Test prediction
