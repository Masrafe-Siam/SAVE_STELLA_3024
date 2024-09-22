function onClickedPredictPlantType() {
    console.log("Predict plant type button clicked");
    var soilTemp = document.getElementById("uiSoilTemperature");
    var soilPH = document.getElementById("uiSoilPH");
    var predictedPlantType = document.getElementById("uiPredictedPlantType");

    var url = "http://127.0.0.1:5000/predict_plant_type"; // Ensure Flask server is running

    $.post(url, {
        soil_temp: parseFloat(soilTemp.value),  // Corrected key
        soil_ph: parseFloat(soilPH.value)       // Corrected key
    },function(data, status) {
        console.log(data.predicted_plant_type);
        predictedPlantType.innerHTML = "<h2>" + data.predicted_plant_type + "</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
}

window.onload = onPageLoad;
