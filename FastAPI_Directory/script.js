async function predict(){
    const data = {
        sepal_length: parseFloat(document.getElementById("sl").value),
        sepal_width: parseFloat(document.getElementById("sw").value),
        petal_length: parseFloat(document.getElementById("pl").value),
        petal_width: parseFloat(document.getElementById("pw").value)
    };

    const res = await fetch("http://127.0.0.1.8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("result").innserText = "Prediction: " + result.prediction;


}

