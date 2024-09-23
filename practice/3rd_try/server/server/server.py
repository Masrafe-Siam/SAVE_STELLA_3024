from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_column_names', methods=['GET'])
def get_column_names():
    response = jsonify({
        'columns': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_land_type', methods=['POST'])
def predict_land_type():
    try:
        Dissolved_Oxygen = float(request.form['dissolved_oxygen'])  # Match the name used in app.js
        pH = float(request.form['waterPH'])  # Match the name used in app.js

        predicted_land_type = util.get_predicted_plant_type(Dissolved_Oxygen, pH)

        response = jsonify({
            'predicted_land_type': str(predicted_land_type)  # Convert to string if necessary
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error as JSON

if __name__ == "__main__":
    print("Starting Python Flask Server for Plant Type Prediction...")
    util.load_saved_artifacts()
    app.run()
