# AI Vegetable Quality Detection System

## Overview

This project is an AI-powered system that detects the quality of vegetables from an image.
Users can upload a photo, and the system returns:

* Quality Grade (A / B / C)
* Freshness Score (%)
* AI Confidence
* Explanation

The goal is to help farmers, vendors, and buyers quickly assess produce quality and reduce waste.

---

## How It Works

**Flow:**
User → Frontend → Backend API → AI Model → Backend → Frontend

1. User uploads an image
2. Frontend sends it to the backend API
3. Backend processes the image
4. AI model predicts freshness
5. Backend converts prediction into grade and explanation
6. Results are displayed on the UI

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI

### AI / ML

* TensorFlow / Keras (.h5 model)
* Teachable Machine

---

## Project Structure

```
veg-quality-detector/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── grading.py
│   ├── model/
│   │   ├── model.h5
│   │   └── labels.txt
│   └── requirements.txt
│
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd veg-quality-detector
```

---

### 2. Backend setup

```
cd backend
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
```

Run backend:

```
python -m uvicorn main:app --reload
```

---

### 3. Frontend setup

```
cd ../frontend
python -m http.server 5500
```

Open:

```
http://localhost:5500
```

---

## API Endpoint

### POST `/analyze`

**Request:**

* Multipart form-data
* Field: `file` (image)

**Response:**

```
{
  "grade": "A",
  "freshness": 95,
  "confidence": 0.98,
  "message": "Fresh with no visible defects"
}
```

---

## Features

* Real-time AI inference
* Clean and simple user interface
* Grade and explanation mapping
* End-to-end system integration
* Robust error handling

---

## Development Workflow

The team followed a structured GitHub-based workflow:

* Used feature branches for development
* Maintained a `dev` branch for integration
* Merged stable code into `main`
* Used pull requests for collaboration and review
* Regularly pulled updates to stay in sync

This ensured smooth collaboration and minimized conflicts during development.

---

## Team

* Sohan Kotian
* Nishant BM
* Anush Koingodi
* Vignesh RK

All team members actively used GitHub for version control, collaboration, and managing the development workflow.

---

## Future Improvements

* Camera-based image capture
* Deployment for public access
* Improved model accuracy with larger datasets
* Enhanced UI/UX

---

## Conclusion

This project demonstrates a complete AI-powered pipeline from image input to actionable insights, built with a focus on usability, speed, and real-world application.
