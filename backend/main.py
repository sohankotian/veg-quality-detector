from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

from grading import get_grade

app = FastAPI()

# Allow frontend requests (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = tf.keras.models.load_model("models/model.h5")

# Load labels
with open("model/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]


# Image preprocessing (Teachable Machine style)
def preprocess_image(image: Image.Image):
    image = image.resize((224, 224))  # common size
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Preprocess
        img_array = preprocess_image(image)

        # Predict
        predictions = model.predict(img_array)
        confidence = float(np.max(predictions))
        index = int(np.argmax(predictions))
        label = labels[index]

        # Clean label (Teachable Machine adds numbers)
        label = label.split(" ")[-1].lower()

        # Grading logic
        grade, freshness, message = get_grade(label, confidence)

        return {
            "grade": grade,
            "freshness": freshness,
            "confidence": round(confidence, 2),
            "message": message
        }

    except Exception as e:
        return {
            "error": str(e)
        }