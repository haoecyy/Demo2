import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Welcome to Streamlit")
st.write("Hello guys and **Bold Text**")
st.write("my name is arina")
st.write({"Name":"Alice","Age":3})
st.write("**Bold text**")
st.write("Hello guys and **Bold Text**")
st.header("Section 1: Introduction")
age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")
option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

