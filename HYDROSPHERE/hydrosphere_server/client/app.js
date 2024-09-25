function onClickedPredictAquaticEnvironment() {
    console.log("Predict aquatic environment button clicked");
    var dissolved_oxygen = document.getElementById("uiDissolvedOxygen");
    var salinities = document.getElementById("uiSalinities");
    var predictedAquaticEnvironment = document.getElementById("uiPredictedAquaticEnvironment");

    var url = "http://127.0.0.1:5000/predict_aquatic_environment"; // Updated URL

    $.post(url, {
        dissolved_oxygen: parseFloat(dissolved_oxygen.value),  // Send correct variable names
        salinities: parseFloat(salinities.value)  // Send correct variable names
    }, function(data, status) {
        console.log(data.predicted_environment);
        predictedAquaticEnvironment.innerHTML = "<h2>" + data.predicted_environment + "</h2>";  // Updated for 'aquatic environment'
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
}

window.onload = onPageLoad;
