import streamlit as st
import numpy as np
import joblib

model = joblib.load("diabetes_model.pkl")

st.title("🩺 Disease Prediction System - Diabetes")
st.write("Enter patient data to predict diabetes status:")

preg = st.number_input("Pregnancies", 0, 20, step=1)
glucose = st.number_input("Glucose", 0, 200, step=1)
bp = st.number_input("Blood Pressure", 0, 150, step=1)
skin = st.number_input("Skin Thickness", 0, 100, step=1)
insulin = st.number_input("Insulin", 0, 900, step=1)
bmi = st.number_input("BMI", 0.0, 70.0, step=0.1)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, step=0.01)
age = st.number_input("Age", 1, 120, step=1)

if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🧬 Prediction: Diabetic")
    else:
        st.success("✅ Prediction: Not Diabetic")
