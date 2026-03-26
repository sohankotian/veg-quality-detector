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
    formData.append("file", file); // IMPORTANT: must match backend

    try {
        const response = await fetch("http://192.168.x.x:8000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        displayResult(data);

    } catch (error) {
        console.error("API Error:", error);
        alert("Failed to analyze image. Check backend.");
    }
});