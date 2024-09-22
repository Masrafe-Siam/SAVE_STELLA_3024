function onClickedPredictPlantType() {
    console.log("Predict plant type button clicked");

    var dissolvedOxygen = document.getElementById("uiDissolvedOxygen");
    var waterTemp = document.getElementById("uiTemperature");
    var waterPH = document.getElementById("uiPH");
    var predictedPlantType = document.getElementById("uiPredictedPlantType");

    var url = "http://127.0.0.1:5000/predict_plant_type"; // Flask server URL

    $.post(url, {
        dissolved_oxygen: parseFloat(dissolvedOxygen.value),
        temperature: parseFloat(waterTemp.value),
        ph: parseFloat(waterPH.value)
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