import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/house_model.pkl")

print(model.feature_names_in_)

# Sample house (same feature order as training)
house = pd.DataFrame([{
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 2000,
    "sqft_lot": 5000,
    "floors": 2,
    "waterfront": 0,
    "view": 0,
    "condition": 3,
    "grade": 8,
    "sqft_above": 1800,
    "sqft_basement": 200,
    "yr_built": 1995,
    "yr_renovated": 0,
    "zipcode": 98052,
    "lat": 47.63,
    "long": -122.13,
    "sqft_living15": 2000,
    "sqft_lot15": 5000
}])

prediction = model.predict(house)

print(f"Predicted House Price: ${prediction[0]:,.2f}")