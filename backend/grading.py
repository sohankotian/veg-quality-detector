def get_grade(label, confidence):
    confidence_percent = int(confidence * 100)

    if label == "fresh":
        freshness = confidence_percent

        if confidence > 0.85:
            return "A", freshness, "Fresh with no visible defects"
        else:
            return "B", freshness, "Slight imperfections detected"

    elif label == "rotten":
        freshness = 100 - confidence_percent  # 🔥 KEY FIX

        if confidence > 0.85:
            return "C", freshness, "Visible spoilage or damage"
        else:
            return "B", freshness, "Some spoilage detected"

    return "B", 50, "Uncertain quality"