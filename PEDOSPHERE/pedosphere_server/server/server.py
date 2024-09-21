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

@app.route('/predict_plant_type', methods=['POST'])
def predict_plant_type():
    soil_temp = float(request.form['soil_temp'])
    soil_ph = float(request.form['soil_ph'])

    response = jsonify({
        'predicted_plant_type': util.get_predicted_plant_type(soil_temp, soil_ph)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Plant Type Prediction...")
    util.load_saved_artifacts()
    app.run()
