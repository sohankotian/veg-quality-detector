from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tf_keras as keras
import numpy as np
from PIL import Image
import io

from grading import get_grade

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model (safe mode)
model = keras.models.load_model("model/model.h5", compile=False)

# Load labels
with open("model/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]


# Image preprocessing
def preprocess_image(image: Image.Image):
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        print("📥 Received file")

        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        print("🖼 Image loaded")

        img_array = preprocess_image(image)

        print("🤖 Running prediction")

        predictions = model.predict(img_array)

        print("✅ Prediction done:", predictions)

        confidence = float(np.max(predictions))
        index = int(np.argmax(predictions))

        raw_label = labels[index]
        print("🏷 Raw label:", raw_label)

        # 🔥 FIX: robust label extraction
        label = raw_label.split(" ")[-1].strip().lower()

        # Extra safety (handles unexpected formats)
        if "fresh" in label:
            label = "fresh"
        elif "rotten" in label:
            label = "rotten"

        print("✅ Clean label:", label)

        grade, freshness, message = get_grade(label, confidence)

        return {
            "grade": grade,
            "freshness": freshness,
            "confidence": round(confidence, 2),
            "message": message
        }

    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}