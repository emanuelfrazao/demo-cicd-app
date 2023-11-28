import streamlit as st
from utils import calculate_bmi

st.title("greatest BMI app")

st.write("Enter your height in meters, please")
height = st.number_input("Height")

st.write("Enter your weight in kilograms")
weight = st.number_input("Weight")

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write("Your BMI is: ", bmi)