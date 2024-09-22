from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_column_names', methods=['GET'])
def get_column_names():
    response = jsonify({
        'columns': util.get_data_columns()
    })
    return response

@app.route('/predict_plant_type', methods=['POST'])
def predict_plant_type():
    try:
        Dissolved_Oxygen = float(request.form['Dissolved_Oxygen'])
        Temperature = float(request.form['Temperature'])
        pH = float(request.form['pH'])

        predicted_plant_type = util.get_predicted_plant_type(Dissolved_Oxygen, Temperature, pH)

        response = jsonify({
            'predicted_plant_type': predicted_plant_type
        })
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server for Plant Type Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)  # Set debug=True for easier troubleshooting
