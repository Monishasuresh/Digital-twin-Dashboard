import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Read the CSV file
data = pd.read_csv('C:/Users/admin/Desktop/Capstone Project/Code/Data/Soil data.csv')

# Split the data into features (NPK values) and labels
X = data.iloc[:, 0:3]
y = data.iloc[:, 3]

# Set feature names
feature_names = ['N', 'P', 'K']
X.columns = feature_names

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy
print("Model Accuracy:", accuracy)

# Predict the fertility of a new soil sample
new_sample = [[6, 7, 5]]  # NPK values of the new soil sample
prediction = model.predict(new_sample)
print(type(prediction))
# Interpret the prediction
if prediction[0] == "Fertile":
    print("The soil is predicted to be fertile.")
else:
    print("The soil is predicted to be infertile.")

# Save the model
joblib.dump(model, "Fertility.joblib")
