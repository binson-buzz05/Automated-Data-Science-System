import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Automated Data Science System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Automated Data Science System")

st.write(
    "Upload a CSV file to automatically perform "
    "data profiling, cleaning, visualization and machine learning."
)

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("📊 Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("🔍 Data Profiling")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    st.subheader("📋 Data Types")

    st.dataframe(
        df.dtypes.astype(str)
    )