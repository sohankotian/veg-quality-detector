##  Project Flow

This document explains the complete working flow of the **Vegetable Quality Detector** system.

---

### 1. Data Acquisition 

- Collect images of vegetables (e.g., tomatoes).
- Ensure images include both **fresh** and **rotten** categories.
- Organize dataset into folders:

- 
---

### 2. Data Preprocessing 

- Load images using Python.
- Resize images to required dimensions.
- Normalize pixel values.
- Assign labels (fresh = 0, rotten = 1).

Run preprocessing script:


---

### 3. Model Training 

- Use **TensorFlow / Keras** to train the model.
- Input: Preprocessed images
- Output: Classification (Fresh / Rotten)

Run training:


- Trained model is saved as:

- 
---

### 4. Backend Processing ⚙️

- Load trained model (`model.h5`)
- Accept image input
- Perform prediction using the model
- Return output label:
  - "Fresh"
  - "Rotten"

---

### 5. Frontend Interaction 

- Built using:
  - HTML
  - CSS
  - JavaScript

- Features:
  - Upload vegetable image
  - Send image to backend
  - Display prediction result

Files:


---

### 6. Prediction Flow 🔄

1. User uploads image from frontend  
2. Image is sent to backend  
3. Backend processes image  
4. Model predicts quality  
5. Result sent back to frontend  
6. Output displayed to user  

---

### 7. Output 

- Final result shown to user:
  -  Fresh Vegetable
  -  Rotten Vegetable

---

##  Summary

This project combines:
- Machine Learning (TensorFlow/Keras)
- Backend Processing (Python)
- Frontend Development (HTML, CSS, JS)

to create a complete **Vegetable Quality Detection System**.


