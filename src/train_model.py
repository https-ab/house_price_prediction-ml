import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Load dataset
data = pd.read_csv("data/house_sales.csv")


# Remove unnecessary columns
data = data.drop(columns=["id", "date"])


# Separate features and target
X = data.drop("price", axis=1)
y = data["price"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train model
rf_model.fit(X_train, y_train)


# Save model
joblib.dump(
    rf_model,
    "models/house_model.pkl"
)


print("Model trained and saved successfully!")