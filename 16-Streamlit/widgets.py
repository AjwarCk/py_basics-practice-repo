import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)

st.write(f"Hi {name}, Your age is {age}.")

options = ['Python','JavaScript','C++','Java']
choice = st.selectbox("Choose your favorite language:",options)
st.write(f"{name}, You have selected {choice} language.")

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)