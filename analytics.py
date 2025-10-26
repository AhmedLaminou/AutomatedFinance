import pandas as pd
import plotly.express as px
import streamlit as st

def top_vendors(df, n=5):
    top = df.groupby("Details")["Amount"].sum().sort_values(ascending=False).head(n).reset_index()
    st.subheader(f"🏆 Top {n} Vendors")
    st.dataframe(top, use_container_width=True)
    fig = px.bar(top, x="Details", y="Amount", title=f"Top {n} Vendors by Spending", text="Amount")
    st.plotly_chart(fig, use_container_width=True)

def forecast_expenses(df):
    import numpy as np
    from statsmodels.tsa.holtwinters import ExponentialSmoothing

    forecast_df = pd.DataFrame(columns=["Category", "Forecast_AED"])
    for cat in df["Category"].unique():
        cat_df = df[df["Category"]==cat].groupby(pd.Grouper(key="Date", freq="M"))["Amount"].sum()
        if len(cat_df) < 2:
            forecast_df = pd.concat([forecast_df, pd.DataFrame({"Category":[cat], "Forecast_AED":[cat_df.sum()]})])
            continue
        model = ExponentialSmoothing(cat_df, trend="add", seasonal=None)
        fit = model.fit()
        pred = fit.forecast(1).iloc[0]
        forecast_df = pd.concat([forecast_df, pd.DataFrame({"Category":[cat], "Forecast_AED":[pred]})])
    st.subheader("🔮 Forecast for Next Month")
    st.dataframe(forecast_df, use_container_width=True)