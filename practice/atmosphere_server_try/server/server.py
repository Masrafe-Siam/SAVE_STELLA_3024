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
    air_temp = float(request.form['air_temp'])
    humidity = float(request.form['humidity'])

    response = jsonify({
        'predicted_land_type': util.get_predicted_land_type(air_temp, humidity)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Land Type Prediction...")
    util.load_saved_artifacts()
    app.run()
