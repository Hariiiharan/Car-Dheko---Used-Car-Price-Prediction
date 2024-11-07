import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder 

# Load the trained model
filename = 'E:/streamlit/env/car.pkl'  # Use the correct filename where your model is saved
loaded_model = pickle.load(open(filename, 'rb'))


# Function to predict price
def predict_price(features):
  """
  Predicts the price based on the given features.
  """
  prediction = loaded_model.predict([features])[0]
  return prediction


# Streamlit app
st.title("Car Price Prediction App")
st.image("C:/Users/ADMIN/Downloads/car.jpg")

st.sidebar.header("Filter Options")

# Input fields
bt = st.sidebar.selectbox("Body Type", ['Select One','Hatchback', 'Sedan', 'SUV', 'Minivans' , 'MUV' , 'Wagon'])
fuel_type = st.sidebar.selectbox("Fuel Type", ['Select One','Petrol', 'Diesel', 'CNG', 'LPG'])
transmission = st.sidebar.selectbox("Transmission", ['Select One','Manual', 'Automatic'])
color = st.sidebar.selectbox("Color", ['Select One','White', 'Black', 'Silver', 'Grey', 'Red', 'Blue', 'Others','Maroon',
                               'Brown','Yellow','Orange','Violet','Titanium','Purple','Beige'])
city = st.sidebar.selectbox("City", ['Select One','Chennai', 'Bangalore', 'Kolkata', 'Jaipur', 'Delhi', 'Hyderabad'])
steering_type = st.sidebar.selectbox("Steering Type", ['Select One','Power', 'Manual', 'Hydraulic'])
insurance_validity = st.sidebar.selectbox("Insurance Validity", ['Select One','Third Party', 'Zero Dep', 'Comprehensive', 'Not Available'])
Seats = st.sidebar.number_input("Seats Capacity", min_value=0, max_value=10)
mileage = st.sidebar.slider("Mileage (Km/L)", min_value=0.0, max_value=50.0)
modelYear = st.sidebar.number_input("Model Year", min_value=0, max_value=2023)
km = st.sidebar.slider("Kilometer" , min_value=0, max_value=200000)
ownerNo = st.sidebar.number_input("Owner", min_value=0, max_value=4)
Engine = st.sidebar.slider("Engine Displacement (CC)", min_value=000, max_value=2000)

# Encode categorical features
le = LabelEncoder()
bt = le.fit_transform([bt])[0]
fuel_type = le.fit_transform([fuel_type])[0]
transmission = le.fit_transform([transmission])[0]
color = le.fit_transform([color])[0]
city = le.fit_transform([city])[0]
steering_type = le.fit_transform([steering_type])[0]
insurance_validity = le.fit_transform([insurance_validity])[0]

# Prepare features for prediction
features = [bt, fuel_type, transmission, color, city, steering_type, insurance_validity, Seats, 
            mileage, modelYear, km, ownerNo, Engine]


#  Predict button
if st.button("Predict Price"):
    try:
        prediction = predict_price(features)
        st.success(f"Predicted Price: ₹{prediction:,.2f} lakhs")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")