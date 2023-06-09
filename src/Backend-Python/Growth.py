import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from tensorflow import keras
import joblib

# Load the dataset
data = pd.read_csv("C:/Users/admin/Desktop/Capstone Project/Code/Data/Data.csv")  # Replace with your dataset filename

# Split features and labels
X = data[['Plant Height', 'Plant Width', 'Chlorophyll Content', 'Temperature', 'Humidity', 'Light']]
y = data['Growth']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Predict plant growth for new data
new_data = pd.DataFrame({
    'Plant Height': [102, 89, 23],
    'Plant Width': [45, 38, 52],
    'Chlorophyll Content': [0.3, 0.8, 0.1],
    'Temperature': [25, 28, 27],
    'Humidity': [60, 75, 80],
    'Light': [700, 600, 200]
})
predictions = model.predict(new_data)
print(type(predictions))

joblib.dump(model , "Growth.joblib")