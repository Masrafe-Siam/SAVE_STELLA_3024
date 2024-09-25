import pickle
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder

__model = None
__data_columns = None
__label_encoder = None  # Label encoder for decoding

def get_predicted_aquatic_environment(Dissolved_Oxygen, salinities):
    # Validate the input values
    if Dissolved_Oxygen < 1.0 or Dissolved_Oxygen > 20.0:
        return 'Invalid Dissolved Oxygen value. Must be between 1.0 and 20.0 mg/L.'
    if salinities < 0 or salinities > 60.0:  # Adjust salinity limits based on your data
        return 'Invalid salinity value. Must be between 0 and 60 PSU.'

    # Prepare the input for the model
    x = np.array([Dissolved_Oxygen, salinities]).reshape(1, -1)

    # Predict the index of the aquatic environment
    predicted_index = __model.predict(x)[0]

    # Decode the index back to the aquatic environment using the label encoder
    if __label_encoder is not None:
        predicted_label = __label_encoder.inverse_transform([predicted_index])
        print(f"Predicted Index: {predicted_index}")  # Print the predicted index
        print(f"Predicted Label: {predicted_label[0]}")  # Print the predicted label
        return predicted_label[0]  # Return the predicted environment as a string
    else:
        return 'Label encoder not loaded properly.'

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns, __label_encoder

    # Load the column names
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        # Load the machine learning model
        with open('./artifacts/hydrosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    # Load the label encoder
    with open('./artifacts/label_encoder.pickle', 'rb') as f:
        __label_encoder = pickle.load(f)

    # Print the classes for debugging purposes
    print("Label Encoder Classes:", __label_encoder.classes_)

    print("Loading saved artifacts... done")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    # Test prediction with sample values
    print(get_predicted_aquatic_environment(8, 20))  # Example input for prediction
