import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("../dataset/student.csv")

# Clean columns
data.columns = data.columns.str.strip().str.lower()

print(data.head())
print(data.dtypes)

# Features
X = data[['studytime', 'absences', 'g1', 'g2']]

# Target
y = data['g3']

print(X.head())
print(y.head())

# Train model
model = LinearRegression()
model.fit(X, y)

# Accuracy
score = model.score(X, y)
print("Model Accuracy:", score)

# Save model
joblib.dump(model, "../backend/student_model.pkl")

print("Model trained successfully!")