def get_grade(label, confidence):
    if label == "fresh" and confidence > 0.85:
        return "A", 90 + int(confidence * 10), "Fresh with no visible defects"
    elif confidence > 0.6:
        return "B", 60 + int(confidence * 20), "Minor discoloration or spots"
    else:
        return "C", 30 + int(confidence * 30), "Visible spoilage or damage"