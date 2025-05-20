import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("student_data.csv")

# Encode categorical data
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['School_Type'] = le.fit_transform(df['School_Type'])
df['Passed'] = df['Passed'].map({'Yes': 1, 'No': 0})

# Features & label
X = df.drop(['StudentID', 'Passed'], axis=1)
y = df['Passed']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "exam_pass_model.pkl")
