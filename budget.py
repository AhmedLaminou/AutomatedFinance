import streamlit as st

def init_budgets(categories):
    if "budgets" not in st.session_state:
        st.session_state.budgets = {cat: 0.0 for cat in categories}

def check_budget(df):
    alerts = []
    if "budgets" in st.session_state:
        spent = df.groupby("Category")["Amount"].sum()
        for cat, limit in st.session_state.budgets.items():
            if cat in spent and spent[cat] > limit > 0:
                alerts.append(f"⚠️ {cat} exceeded: {spent[cat]:.2f} > {limit:.2f}")
    return alerts

def check_budget(df):
    alerts = []
    for cat, limit in st.session_state.budgets.items():
        spent = df[df["Category"]==cat]["Amount"].sum()
        if spent > limit:
            alerts.append(f"⚠️ Budget exceeded in {cat}: {spent:.2f} AED (Limit: {limit:.2f})")
        elif spent > 0.8*limit:
            alerts.append(f"🔔 Approaching budget in {cat}: {spent:.2f} AED / {limit:.2f} AED")
    return alerts