import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the pre-trained model and scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# Define expected input layout
st.title("Insurance Cost Prediction App")
st.markdown("### Enter the details below to predict insurance costs.")

# Input fields
st.write("Min Age: 3 years, Max Age: 90 years")
age = st.number_input("Age", min_value=3, max_value=90)
gender = st.selectbox("Sex", ("Female", "Male"))
st.write("Min BMI: 14.0, Max BMI: 54.0")
bmi = st.number_input("BMI (Body Mass Index)", min_value=14.0, max_value=54.0, step=0.1)
children = st.number_input("Number of Children", min_value=0)
smoker = st.selectbox("Smoker", ("Yes", "No"))
region = st.selectbox("Region", ("Northeast", "Northwest", "Southeast", "Southwest"))

# Predict button
if st.button("Predict Amount"):
    # Encode inputs
    gender_encoded = 0 if gender == "Female" else 1
    smoker_encoded = 1 if smoker == "Yes" else 0
    region_mapping = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
    region_encoded = region_mapping[region]

    # Create DataFrame
    input_data = pd.DataFrame([[age, gender_encoded, bmi, children, smoker_encoded, region_encoded]],
                              columns=["age", "sex", "bmi", "children", "smoker", "region"])

    # Scale data
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Display results
    st.success(f"Predicted Insurance Cost: ${prediction[0]:,.2f}")
    st.balloons()
    st.write("### Thank you for using the Insurance Cost Prediction App!")
