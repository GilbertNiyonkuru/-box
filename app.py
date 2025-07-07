import streamlit as st
from recommendations import analyze_results

st.set_page_config(page_title="Medical AI Assistant", layout="centered")

st.title("🩺 Medical AI Assistant")
st.markdown("Input patient test results to get AI-generated analysis and recommendations.")

with st.form("medical_form"):
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=25.0, value=13.5)
    wbc = st.number_input("White Blood Cell Count (10^9/L)", min_value=0.0, max_value=20.0, value=6.5)
    platelets = st.number_input("Platelet Count (10^9/L)", min_value=0.0, max_value=1000.0, value=250.0)
    glucose = st.number_input("Fasting Blood Glucose (mg/dL)", min_value=0.0, max_value=300.0, value=90.0)

    submitted = st.form_submit_button("Analyze")

if submitted:
    patient_data = {
        "hemoglobin": hemoglobin,
        "wbc": wbc,
        "platelets": platelets,
        "glucose": glucose
    }

    st.subheader("🧠 AI Recommendations:")
    results = analyze_results(patient_data)
    for r in results:
        st.write(f"✅ {r}")
