import pickle
import json
import numpy as np

__model = None
__data_columns = None

def get_predicted_plant_type(dissolved_oxygen, temperature, ph):
    # Validate inputs
    if not (1.0 <= dissolved_oxygen <= 15.0):
        return 'Invalid dissolved oxygen value'
    if not (5 <= temperature <= 30):
        return 'Invalid temperature value'
    if not (4.0 <= ph <= 9.5):
        return 'Invalid pH value'

    # Prepare the input for the model
    x = np.array([dissolved_oxygen, temperature, ph]).reshape(1, -1)
    return __model.predict(x)[0]

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
    print(get_predicted_plant_type(7, 25, 5))  # Test prediction