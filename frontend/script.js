const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const analyzeBtn = document.getElementById("analyzeBtn");

const resultBox = document.getElementById("result");
const gradeEl = document.getElementById("grade");
const freshnessEl = document.getElementById("freshness");
const confidenceEl = document.getElementById("confidence");
const messageEl = document.getElementById("message");

// Show image preview
imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.hidden = false;
    }
});

// Analyze button click
analyzeBtn.addEventListener("click", async () => {
    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://localhost:8000/analyze", {
            method: "POST",
            body: formData
        });

        console.log("STATUS:", response.status);

        const data = await response.json();
        console.log("DATA:", data);

        // 🔥 Always display result if we got JSON
        displayResult(data);

    } catch (error) {
        console.error("FETCH ERROR:", error);
        alert("Something went wrong. Check console.");
    }
});
function displayResult(data) {
    console.log("DISPLAYING:", data);

    resultBox.classList.remove("hidden");

    gradeEl.textContent = data.grade;
    freshnessEl.textContent = data.freshness;
    confidenceEl.textContent = data.confidence;
    messageEl.textContent = data.message;
}