import streamlit as st
import pickle
import numpy as np
model  = pickle.load(open("heart_model.pkl", "rb"))
features = pickle.load(open("features.pkl","rb"))
st.title("Heart Disease Predictor")
inputs =[]
for features in feature:
  value = st.number_input(feature, value=0.0)
  inputs.append(value)
if st.button("Predict"):
  prediction = model.predict([inputs])[0]
  st.success(f"Predcited Heart Diseases:{prediction:.2f}")  
  
