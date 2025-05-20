import pandas as pd
import random

# Seed for reproducibility
random.seed(42)

# Options
genders = ["Male", "Female"]
school_types = ["Public", "Private"]

data = []

for student_id in range(1001, 1101):  # 100 students
    math = random.randint(30, 95)
    english = random.randint(30, 90)
    science = random.randint(30, 95)
    attendance = random.randint(50, 100)
    gender = random.choice(genders)
    school_type = random.choice(school_types)

    # Passing rule (basic logic): if average score and attendance are good
    average_score = (math + english + science) / 3
    passed = "Yes" if average_score >= 50 and attendance >= 70 else "No"

    data.append([
        student_id, math, english, science, attendance,
        gender, school_type, passed
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "StudentID", "Grade9_Math", "Grade9_English", "Grade9_Science",
    "Attendance", "Gender", "School_Type", "Passed"
])

# Save to CSV
df.to_csv("student_data.csv", index=False)
print("Dummy dataset 'student_data.csv' created with 100 rows.")
