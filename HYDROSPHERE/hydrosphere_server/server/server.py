from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_column_names', methods=['GET'])
def get_column_names():
    try:
        columns = util.get_data_columns()
        response = jsonify({
            'columns': columns
        })
    except Exception as e:
        response = jsonify({
            'error': str(e)
        })
        response.status_code = 500

    return response

@app.route('/predict_plant_type', methods=['POST'])
def predict_plant_type():
    try:
        # Parse JSON data from the request body
        data = request.get_json()

        # Retrieve values from the parsed data
        dissolved_oxygen = float(data.get('dissolved_oxygen'))
        temperature = float(data.get('temperature'))
        ph = float(data.get('ph'))

        # Get prediction from the util function
        predicted_plant_type = util.get_predicted_plant_type(dissolved_oxygen, temperature, ph)

        # Convert the prediction (if needed) to native Python types before jsonify
        if isinstance(predicted_plant_type, np.integer):
            predicted_plant_type = int(predicted_plant_type)
        elif isinstance(predicted_plant_type, np.floating):
            predicted_plant_type = float(predicted_plant_type)

        # Send the response with the predicted plant type
        response = jsonify({
            'predicted_plant_type': predicted_plant_type
        })
    except KeyError as e:
        response = jsonify({
            'error': f"Missing parameter: {str(e)}"
        })
        response.status_code = 400
    except Exception as e:
        response = jsonify({
            'error': str(e)
        })
        response.status_code = 500

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Plant Type Prediction based on Dissolved Oxygen, Temperature, and pH...")
    util.load_saved_artifacts()
    app.run()
