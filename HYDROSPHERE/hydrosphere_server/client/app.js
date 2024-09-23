function onClickedPredictLandType() {
    console.log("Predict plant type button clicked");
    var dissolved_oxygen = document.getElementById("uiDissolvedOxygen");
    var waterPH = document.getElementById("uiPH");
    var predictedLandType = document.getElementById("uiPredictedPlantType");

    var url = "http://127.0.0.1:5000/predict_land_type"; // Ensure Flask server is running

    $.post(url, {
        dissolved_oxygen: parseFloat(dissolved_oxygen.value),  // Send correct variable names
        waterPH: parseFloat(waterPH.value)  // Send correct variable names
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
