import streamlit as st
import pandas as pd
import numpy as np

# Set the title of your web app
st.title("🚀 My First Streamlit App")

# Add some simple text
st.write("Welcome! This app generates random data and plots a dynamic chart in seconds.")

# Create an interactive slider widget
num_points = st.slider("Select number of data points:", min_value=10, max_value=500, value=100)

# Generate a random dataset based on slider input
chart_data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['Metric A', 'Metric B']
)

# Render an interactive line chart
st.subheader("Interactive Visualizations")
st.line_chart(chart_data)

# Add a toggle checkbox to show/hide raw data
if st.checkbox("Show raw data table"):
    st.dataframe(chart_data)
