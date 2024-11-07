# # Car Price Prediction App

This project is a machine learning-based web application for predicting car prices based on various car attributes. The model was trained using data on car features such as body type, fuel type, engine size, and more. The app is deployed using **Streamlit**, making it easy for users to interact with the model and get predictions in real-time.

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
5. [Model Development](#model-development)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Results](#results)
9. [Conclusion](#conclusion)
10. [Future Work](#future-work)
11. [Contributing](#contributing)
12. [License](#license)

---

## Project Description

The **Car Price Prediction App** uses machine learning to predict the price of a car based on a variety of features. It takes into account factors like the car's body type, engine displacement, fuel type, transmission type, and more to provide a price estimate.

This project consists of two main parts:
1. **Data Preprocessing and Model Training**: Includes data cleaning, feature selection, model building, and model evaluation.
2. **Web Application**: An interactive web application built with Streamlit that allows users to input car attributes and receive a predicted price.

## Features

- **User-friendly Interface**: The app provides an easy-to-use interface where users can select or input car features, such as body type, fuel type, transmission, mileage, etc.
- **Real-time Predictions**: Users can instantly predict the price of a car based on the given inputs.
- **Feature Encoding**: Categorical features are automatically encoded to ensure smooth prediction by the model.
- **Model Training**: The Random Forest model was used to predict the car prices, providing good accuracy for this task.

## Dataset

The dataset used for training contains car features, which include:
- **Body Type** (e.g., Sedan, SUV, Hatchback)
- **Fuel Type** (e.g., Petrol, Diesel, CNG, LPG)
- **Transmission** (e.g., Manual, Automatic)
- **Color** (e.g., White, Black, Silver)
- **City** (e.g., Chennai, Bangalore, Delhi)
- **Steering Type** (e.g., Power, Manual)
- **Insurance Validity** (e.g., Third Party, Zero Dep)
- **Seats Capacity** (e.g., 5, 7)
- **Mileage (Km/L)**
- **Model Year**
- **Kilometers Driven**
- **Owner Number**
- **Engine Displacement (CC)**

The target variable is the **price** of the car.

## Exploratory Data Analysis (EDA)

Before training the model, the data was analyzed to understand key relationships between features and the target variable. This involved:
- Visualizing distributions of continuous variables such as mileage, engine displacement, and kilometers driven.
- Checking the correlation between features to understand which ones influence the car price the most.
- Detecting and handling outliers and missing values.

## Model Development

### Data Preprocessing

- **Handling Missing Data**: Missing values were imputed using appropriate strategies. For instance, missing city names in the 'RTO' column were filled based on other available information.
- **Encoding Categorical Data**: Categorical variables like body type, fuel type, transmission, and color were label-encoded.
- **Feature Scaling**: Features like mileage and engine displacement were scaled to ensure uniformity in the prediction model.

### Model Training

The machine learning model was developed using **Random Forest Regressor**. The steps involved:
- **Model Selection**: Random Forest was selected for its high performance and robustness in handling complex datasets with both categorical and continuous features.
- **Hyperparameter Tuning**: Hyperparameters were fine-tuned using cross-validation to optimize performance.
- **Model Evaluation**: The model was evaluated using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

