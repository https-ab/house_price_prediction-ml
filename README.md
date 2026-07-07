# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project predicts house prices using Machine Learning based on various property features such as the number of bedrooms, bathrooms, living area, condition, grade, location, and more.

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, comparison of multiple algorithms, and model serialization.

---

## 🚀 Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Linear Regression model
* Random Forest Regressor model
* Model performance comparison
* Model evaluation using MAE, MSE, and R² Score
* Save the trained model using Joblib
* Predict house prices using the saved model

---

## 📂 Project Structure

```text
house_price_prediction-ml/
│
├── data/
│   └── house_sales.csv
│
├── models/
│   └── house_model.pkl
│
├── notebooks/
│   └── house_prediction.ipynb
│
├── src/
│   ├── train_model.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains information about residential properties, including:

* Bedrooms
* Bathrooms
* Living Area
* Lot Area
* Floors
* Waterfront
* View
* Condition
* Grade
* Above Ground Area
* Basement Area
* Year Built
* Year Renovated
* Zipcode
* Latitude
* Longitude
* Nearby Living Area
* Nearby Lot Area

### Target Variable

* **Price**

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook
* Git & GitHub

---

## 🤖 Machine Learning Models

### 1. Linear Regression

Used as the baseline regression model.

### 2. Random Forest Regressor

Used to improve prediction accuracy by learning complex relationships in the dataset.

---

## 📈 Model Evaluation

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Example Results

| Model             |               MAE |               MSE |          R² Score |
| ----------------- | ----------------: | ----------------: | ----------------: |
| Linear Regression |    127493.342087  |    4.517305e+10   |    0.701190       |
| Random Forest     |    72750.438193   |    2.207688e+10   |    0.853966       |

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/https-ab/house_price_prediction-ml.git
```

Navigate to the project folder:

```bash
cd house_price_prediction-ml
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python src/train_model.py
```

This trains the Random Forest model and saves it to:

```text
models/house_model.pkl
```

---

## ▶️ Predict House Price

```bash
python src/predict.py
```

The script loads the trained model and predicts the price of a sample house.

---

## 📌 Future Improvements

* Hyperparameter tuning
* Feature engineering
* Streamlit web application
* Model deployment
* Cross-validation
* Additional regression model comparisons (e.g., XGBoost)

---

## 📚 Learning Outcomes

Through this project, I learned:

* Data preprocessing techniques
* Exploratory Data Analysis (EDA)
* Regression algorithms
* Model evaluation and comparison
* Saving and loading trained models
* Organizing a machine learning project
* Using Git and GitHub for version control

---

## 👨‍💻 Author

**Anushka Bhasme**