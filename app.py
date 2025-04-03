import pickle
import streamlit as st
import numpy as np

with open("model.pkl","rb")as p:
    model=pickle.load(p)

st.title("Diabetes Prediction")  

st.write("Enter Following Details ")

Pregnancies =st.number_input("Pregnancies",min_value=0.0,format="%.2f")  
Glucose =st.number_input("Glucose",min_value=0.0,format="%.2f") 
BloodPressure =st.number_input("BloodPressure",min_value=0.0,format="%.2f")    
SkinThickness =st.number_input("SkinThickness",min_value=0.0,format="%.2f")  
Insulin =st.number_input("Insulin",min_value=0.0,format="%.2f") 
BMI =st.number_input("BMI",min_value=0.0,format="%.2f")    
DiabetesPedigreeFunction =st.number_input("DiabetesPedigreeFunction",min_value=0.0,format="%.2f")  
Age =st.number_input("Age",min_value=0.0,format="%.2f") 
    
   
if st.button("Examine Your Diabetes"):
    features=np.array([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    predictions=model.predict(features)[0]
    if predictions==0:
        st.success("Negative")
    else:
        st.success("Positive")    
    

#[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]