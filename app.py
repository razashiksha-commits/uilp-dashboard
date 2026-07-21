import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="UILP Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 UILP SEO Dashboard")

uploaded_file = st.file_uploader(
    "Upload your Monthly UILP Report",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.success("Excel uploaded successfully!")

    st.write("### Preview")

    st.dataframe(df.head())

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
