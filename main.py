import streamlit as st
import pandas as pd
import numpy as np

# Add a title and header
st.title("My First Streamlit App")
st.header("Interactive Data Dashboard")

# Take user input
name = st.text_input("Enter your name:")

# Add a slider widget
value = st.slider("Select a range", 0, 100, 25)

# Display interactive charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Conditional display using a button
if st.button("Submit"):
    st.success(f"Hello, {name}! You selected {value}.")
