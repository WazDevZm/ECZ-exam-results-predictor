import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("exam_pass_model.pkl")

# UI
st.title("🇿🇲 Zambian Exam Pass Predictor")
st.write("Enter student data below:")

# Inputs
grade9_math = st.slider("Grade 9 Math (%)", 0, 100, 50)
grade9_eng = st.slider("Grade 9 English (%)", 0, 100, 50)
grade9_sci = st.slider("Grade 9 Science (%)", 0, 100, 50)
attendance = st.slider("Attendance (%)", 0, 100, 80)
gender = st.selectbox("Gender", ["Male", "Female"])
school_type = st.selectbox("School Type", ["Public", "Private"])

# Encoding
gender_encoded = 0 if gender == "Male" else 1
school_type_encoded = 0 if school_type == "Private" else 1

if st.button("Predict"):
    input_data = pd.DataFrame([[grade9_math, grade9_eng, grade9_sci, attendance, gender_encoded, school_type_encoded]],
                              columns=['Grade9_Math', 'Grade9_English', 'Grade9_Science', 'Attendance', 'Gender', 'School_Type'])
    result = model.predict(input_data)[0]
    if result == 1:
        st.success("🎓 The student is likely to PASS!")
    else:
        st.error("❌ The student is likely to FAIL.")
