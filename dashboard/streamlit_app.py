import streamlit as st
import pandas as pd

st.title("Supply Chain Analytics Dashboard")
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())