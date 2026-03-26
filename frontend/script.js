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
    formData.append("image", file);

    try {
        const response = await fetch("http://localhost:8000/analyze", {
            method: "POST",
            body: formData
        });

        // If backend not ready → fallback
        if (!response.ok) throw new Error("Backend not working");

        const data = await response.json();
        displayResult(data);

    } catch (error) {
        console.warn("Using fallback response");

        // 🔥 fallback (from your doc)
        const dummyData = {
            grade: "B",
            freshness: 70,
            confidence: 0.75,
            message: "Minor defects detected"
        };

        displayResult(dummyData);
    }
});

// Display result
function displayResult(data) {
    resultBox.classList.remove("hidden");

    gradeEl.textContent = data.grade;
    freshnessEl.textContent = data.freshness;
    confidenceEl.textContent = data.confidence;
    messageEl.textContent = data.message;
}