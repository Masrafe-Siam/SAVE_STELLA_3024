function onClickedPredictLandType() {
    console.log("Predict land type button clicked");
    var airTemp = document.getElementById("uiairTemperature");
    var Humidity = document.getElementById("uihumidity");
    var predictedLandType = document.getElementById("uiPredictedLandType");

    var url = "http://127.0.0.1:5000/predict_land_type"; // Ensure Flask server is running

    $.post(url, {
        air_temp: parseFloat(airTemp.value),  // Ensure you're using correct variable names
        humidity: parseFloat(Humidity.value)
    },function(data, status) {
        console.log(data.predicted_land_type);
        predictedLandType.innerHTML = "<h2>" + data.predicted_land_type + "</h2>";  // Updated for 'land type'
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
}

window.onload = onPageLoad;
