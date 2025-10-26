import pandas as pd
import streamlit as st

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df.dropna(subset=["Date", "Amount"], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None
