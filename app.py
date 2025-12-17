import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("Please provide your details below:")

age2 = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
color2 = st.selectbox("Choose your favorite color:",
                     ["Red", "Blue", "Green"])

if st.button("Submit"):
    st.success(f"Thank you! Age: {age2}, Favorite Color: {color2}")
