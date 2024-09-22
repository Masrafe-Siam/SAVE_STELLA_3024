function onClickedPredictPlantType() {
    console.log("Predict plant type button clicked");

    var dissolvedOxygen = document.getElementById("uiDissolvedOxygen").value;
    var waterTemp = document.getElementById("uiTemperature").value;
    var waterPH = document.getElementById("uiPH").value;
    var predictedPlantType = document.getElementById("uiPredictedPlantType");

    var url = "http://127.0.0.1:5000/predict_plant_type"; // Flask server URL

    $.ajax({
        url: url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            dissolved_oxygen: parseFloat(dissolvedOxygen),
            temperature: parseFloat(waterTemp),
            ph: parseFloat(waterPH)
        }),
        success: function (data) {
            predictedPlantType.innerHTML = "<h2>" + data.predicted_plant_type + "</h2>";
        },
        error: function (error) {
            console.log("Error:", error);
            predictedPlantType.innerHTML = "<h2>Error occurred while fetching prediction</h2>";
        }
    });
}
