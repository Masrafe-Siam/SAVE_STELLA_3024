import pickle
import json
import numpy as np

__model = None
__data_columns = None

# Example mapping of predicted indices to plant types
plant_types = ['Plant Type 1', 'Plant Type 2', 'Plant Type 3']  # Replace with actual plant types

def get_predicted_plant_type(Dissolved_Oxygen, Temperature, pH):
    """
    Predict the plant type based on dissolved oxygen, temperature, and pH value.
    The function checks for valid ranges and scales the inputs before prediction.
    """
    # Validate the input ranges
    if not (1.0 <= Dissolved_Oxygen <= 15.0):
        return 'Invalid Dissolved Oxygen value. Must be between 1 and 15 mg/L.'
    if not (5 <= Temperature <= 30):
        return 'Invalid Temperature value. Must be between 5°C and 30°C.'
    if not (4.0 <= pH <= 9.5):
        return 'Invalid pH value. Must be between 4.0 and 9.5.'

    # Prepare the input for the model
    x = np.array([Dissolved_Oxygen, Temperature, pH]).reshape(1, -1)

    # Predict the plant type directly from the model output
    predicted_index = __model.predict(x)[0]

    # Return the corresponding plant type
    return plant_types[predicted_index]  # Adjust based on your actual plant types

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
    print(get_predicted_plant_type(4.4, 22.9, 7.5))  # Test prediction
