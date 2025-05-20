# 🇿🇲 Zambian Exam Pass Predictor

This project is a simple web application that predicts whether a Zambian student is likely to pass their exams based on their Grade 9 results, attendance, gender, and school type. The app is built using [Streamlit](https://streamlit.io/) for the user interface and a pre-trained machine learning model for predictions.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Model Training](#model-training)
- [File Descriptions](#file-descriptions)
- [Customization](#customization)
- [Requirements](#requirements)
- [License](#license)

---

## Features

- User-friendly web interface for inputting student data
- Predicts exam pass/fail outcome using a trained model
- Encodes categorical variables (gender, school type) automatically
- Displays clear success/error messages based on prediction

---

## How It Works

1. **User Input:**
   - The user enters student data: Grade 9 Math, English, Science scores, attendance percentage, gender, and school type.
2. **Data Encoding:**
   - Gender and school type are encoded numerically for the model.
3. **Prediction:**
   - The input data is passed to a pre-trained machine learning model (`exam_pass_model.pkl`).
   - The model predicts whether the student is likely to pass (1) or fail (0).
4. **Result Display:**
   - A success message is shown if the student is likely to pass.
   - An error message is shown if the student is likely to fail.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repo-url>
cd ECZ-exam-results-predictor
```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## Usage

- Open the app in your browser (Streamlit will provide a local URL).
- Enter the required student data using the sliders and dropdowns.
- Click the **Predict** button.
- View the prediction result (PASS/FAIL) displayed on the page.

---

## Model Training

- The model is trained using the script `train_model.py` on data from `student_data.csv`.
- The trained model is saved as `exam_pass_model.pkl`.
- To retrain the model with new data, update `student_data.csv` and run:

  ```bash
  python train_model.py
  ```

---

## File Descriptions

- `app.py` : Main Streamlit app for user interaction and prediction.
- `exam_pass_model.pkl` : Pre-trained machine learning model (serialized with joblib).
- `student_data.csv` : Dataset used for training the model.
- `train_model.py` : Script to train and save the model.
- `generate_dataset.py` : (Optional) Script to generate synthetic student data.
- `README.md` : Project documentation.

---

## Customization

- **Model:**
  - You can improve or change the model by editing `train_model.py` and retraining.
- **Features:**
  - Add or remove input features in both `app.py` and `train_model.py` as needed.
- **UI:**
  - Modify the Streamlit UI in `app.py` for a different look or additional information.

---

## Requirements

- Python 3.7+
- streamlit
- pandas
- scikit-learn
- joblib

Install all requirements with:

```bash
pip install -r requirements.txt
```

---

## License

This project is provided for educational purposes. Please check the repository for license details.