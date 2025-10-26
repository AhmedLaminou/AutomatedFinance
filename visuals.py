import plotly.express as px
import streamlit as st

def plot_category_pie(df):
    category_totals = df.groupby("Category")["Amount"].sum().reset_index()
    category_totals = category_totals.sort_values("Amount", ascending=False)
    
    fig = px.pie(
        category_totals,
        values="Amount",
        names="Category",
        title="Expenses by Category",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_monthly_trend(df):
    import plotly.express as px
    import pandas as pd
    import streamlit as st

    # Group by month + category
    monthly = df.groupby([pd.Grouper(key="Date", freq="M"), "Category"])["Amount"].sum().reset_index()

    # Fix: convert Period to Timestamp
    if isinstance(monthly["Date"].iloc[0], pd.Period):
        monthly["Date"] = monthly["Date"].dt.to_timestamp()

    # Plot
    fig = px.line(
        monthly,
        x="Date",
        y="Amount",
        color="Category",
        title="Monthly Expense Trend"
    )
    st.plotly_chart(fig, use_container_width=True)


def combined_chart(df):
    import plotly.graph_objects as go
    cat_totals = df.groupby("Category")["Amount"].sum().reset_index()
    fig = go.Figure()
    # Pie
    fig.add_trace(go.Pie(labels=cat_totals["Category"], values=cat_totals["Amount"], hole=0.4, name="Pie"))
    # Bar
    fig.add_trace(go.Bar(x=cat_totals["Category"], y=cat_totals["Amount"], name="Bar"))
    fig.update_layout(title="Combined View: Pie + Bar", barmode="overlay")
    st.plotly_chart(fig, use_container_width=True)