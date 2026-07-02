import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")

st.title("❤️ Heart Disease Prediction")
st.write("Predict whether a patient is likely to have heart disease.")

st.header("Enter Patient Details")

age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "Chest Pain Type (cp)",
    [0, 1, 2, 3],
    help="0=Typical Angina, 1=Atypical Angina, 2=Non-anginal Pain, 3=Asymptomatic"
)

trestbps = st.number_input(
    "Resting Blood Pressure (trestbps)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Serum Cholesterol (chol)",
    min_value=100,
    max_value=600,
    value=200
)

thalach = st.number_input(
    "Maximum Heart Rate Achieved (thalach)",
    min_value=60,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        thalach,
        exang,
        oldpeak
    ]], columns=[
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "thalach",
        "exang",
        "oldpeak"
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("❤️ Prediction: Heart Disease Detected")
    else:
        st.success("💚 Prediction: No Heart Disease Detected")
