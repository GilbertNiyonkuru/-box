def analyze_results(data):
    results = []

    # Hemoglobin
    if data['hemoglobin'] < 12:
        results.append("Hemoglobin is low. Possible anemia.")
    elif data['hemoglobin'] > 17.5:
        results.append("Hemoglobin is high. Possible dehydration or polycythemia.")

    # WBC
    if data['wbc'] < 4.0:
        results.append("WBC count is low. Possible viral infection or bone marrow issue.")
    elif data['wbc'] > 11.0:
        results.append("WBC count is high. Possible bacterial infection or inflammation.")

    # Platelets
    if data['platelets'] < 150:
        results.append("Low platelet count. Risk of bleeding. Consider further testing.")
    elif data['platelets'] > 400:
        results.append("High platelet count. Could indicate inflammation or blood disorders.")

    # Glucose
    if data['glucose'] < 70:
        results.append("Low fasting glucose. Risk of hypoglycemia.")
    elif data['glucose'] > 100:
        results.append("High fasting glucose. Possible prediabetes or diabetes.")

    if not results:
        results.append("All values appear within the normal range.")

    return results
