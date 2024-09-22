function onClickedPredictPlantType() {
    console.log("Predict plant type button clicked");

    var dissolvedOxygen = document.getElementById("uiDissolvedOxygen");
    var waterTemp = document.getElementById("uiTemperature");
    var waterPH = document.getElementById("uiPH");
    var predictedPlantType = document.getElementById("uiPredictedPlantType");

    var url = "http://127.0.0.1:5000/predict_plant_type"; // Flask server URL

    $.post(url, {
        Dissolved_Oxygen: parseFloat(dissolvedOxygen.value),
        Temperature: parseFloat(waterTemp.value),
        pH: parseFloat(waterPH.value)
    })
    .done(function(data) {
        predictedPlantType.innerHTML = "<h2>Predicted Plant Type: " + data.predicted_plant_type + "</h2>";
        console.log("Prediction successful:", data);
    })
    .fail(function(jqXHR) {
        var errorMsg = jqXHR.responseJSON ? jqXHR.responseJSON.error : "An error occurred";
        predictedPlantType.innerHTML = "<h2>Error: " + errorMsg + "</h2>";
        console.log("Prediction failed:", errorMsg);
    });
}

function onPageLoad() {
    console.log("document loaded");
}

window.onload = onPageLoad;
