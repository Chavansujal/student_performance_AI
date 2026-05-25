async function predictMarks() {

    let hours =
        document.getElementById("hours").value;

    let response = await fetch(
        `https://student-ai-backend.onrender.com/predict?hours=${hours}`
    );

    let data = await response.json();

    document.getElementById("result")
        .innerText =
        "Predicted Marks: " +
        data.predicted_marks;
}