async function predictMarks() {

    let hours =
        document.getElementById("hours").value;

    let response = await fetch(
        `http://127.0.0.1:8000/predict?hours=${hours}`
    );

    let data = await response.json();

    document.getElementById("result")
        .innerText =
        "Predicted Marks: " +
        data.predicted_marks;
}