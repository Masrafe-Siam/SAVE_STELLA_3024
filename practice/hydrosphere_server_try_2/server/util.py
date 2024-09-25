import pickle
import json
import numpy as np

__model = None
__data_columns = None

def get_predicted_plant_type(Dissolved_Oxygen, Sanity):
    if not (0.0 <= Dissolved_Oxygen <= 20.0):
        return 'Invalid Dissolved Oxygen value. Must be between 0 and 20 mg/L.'
    if not (0 <= Sanity <= 60):
        return 'Invalid Sanity value. Must be between 0 and 60.'

    # Prepare the input for the model
    x = np.array([Dissolved_Oxygen, Sanity]).reshape(1, -1)

    # Predict the plant type index
    predicted_index = __model.predict(x)[0]

def load_saved_artifacts():
    print("Loading saved artifacts... start")

    with open('./artifacts/columns_final.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/hydrosphere_model_final.pickle', 'rb') as f:
            __model = pickle.load(f)


    print("Loading saved artifacts... done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_predicted_plant_type(8, 7))  # Test prediction
