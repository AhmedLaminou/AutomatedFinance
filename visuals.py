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
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_totals = df.groupby("Month")["Amount"].sum().reset_index()
    fig = px.bar(monthly_totals, x="Month", y="Amount", title="Monthly Expenses")
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