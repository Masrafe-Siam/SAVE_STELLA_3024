import pickle
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder

__model = None
__data_columns = None
__label_encoder = None  # Add a label encoder for decoding

def get_predicted_plant_type(Dissolved_Oxygen, pH):
    if Dissolved_Oxygen < 1.0 or Dissolved_Oxygen > 15.0:
        return 'Invalid Dissolved Oxygen value. Must be between 1.0 and 15.0 mg/L.'
    if pH < 4.0 or pH > 9.5:
        return 'Invalid pH value. Must be between 4.0 and 9.5.'

    # Prepare the input for the model
    x = np.array([Dissolved_Oxygen, pH]).reshape(1, -1)

    # Predict the plant type index
    predicted_index = __model.predict(x)[0]

    # Decode the index back to the plant type using the label encoder
    predicted_label = __label_encoder.inverse_transform([predicted_index])

    return predicted_label[0]  # Return the predicted plant type as a string

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns, __label_encoder

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/hydrosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    # Load the label encoder
    with open('./artifacts/label_encoder.pickle', 'rb') as f:
        __label_encoder = pickle.load(f)

    print("Loading saved artifacts... done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_predicted_plant_type(8, 7))  # Test prediction
