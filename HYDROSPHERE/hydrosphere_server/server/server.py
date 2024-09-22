from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_column_names', methods=['GET'])
def get_column_names():
    response = jsonify({
        'columns': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_plant_type', methods=['POST'])
def predict_plant_type():
    # Retrieve values from the parsed data
    Dissolved_Oxygen = float(request.form['dissolved_oxygen'])
    Temperature = float(request.form['temperature'])
    pH = float(request.form['ph'])

    predicted_plant_type = util.predict_plant_type(Dissolved_Oxygen, Temperature, pH)

    response = jsonify({
        'predicted_plant_type': str(predicted_plant_type)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Plant Type Prediction based on Dissolved Oxygen, Temperature, and pH...")
    util.load_saved_artifacts()
    app.run()
