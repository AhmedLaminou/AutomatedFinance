import streamlit as st
import pandas as pd
from data_loader import load_transactions
from categorizer import categorize_transactions, add_keyword_to_category, train_predictor, suggest_category
from visuals import plot_category_pie, plot_monthly_trend, combined_chart
from budget import init_budgets, check_budget
from analytics import top_vendors, forecast_expenses
from utils import load_categories, save_categories, save_session, load_session

# ⚡ Streamlit Page Config
st.set_page_config(page_title="💰 Pro Finance Dashboard", page_icon="💹", layout="wide")
st.title("💰 Pro Finance Dashboard")

# Load previous session & categories
load_session()
categories = load_categories()
init_budgets(categories)

# Dark/light theme toggle
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
st.markdown(
    f"<style>body{{background-color:{'#121212' if theme=='Dark' else '#fff'};color:{'#fff' if theme=='Dark' else '#000'}}}</style>",
    unsafe_allow_html=True
)

# Sidebar: Add new category
st.sidebar.header("➕ Add New Category")
new_cat = st.sidebar.text_input("Category Name")
if st.sidebar.button("Add Category") and new_cat:
    if new_cat not in categories:
        categories[new_cat] = []
        save_categories()
        save_session()
        st.rerun()

# Sidebar: Set budgets
st.sidebar.header("💰 Set Budgets")
for cat in categories.keys():
    st.session_state.budgets[cat] = st.sidebar.number_input(
        f"{cat} Budget (AED)", min_value=0.0, value=st.session_state.budgets.get(cat, 0.0)
    )

# Upload CSVs (multi-file support)
uploaded_files = st.file_uploader("Upload CSV(s)", type=["csv"], accept_multiple_files=True)
if uploaded_files:
    df_list = []
    for file in uploaded_files:
        temp_df = load_transactions(file)
        if temp_df is not None:
            df_list.append(temp_df)
    if df_list:
        df = pd.concat(df_list, ignore_index=True)
        df = categorize_transactions(df, categories)
        st.success(f"Merged {len(uploaded_files)} files successfully!")

        # Train predictive categorizer
        predictor = train_predictor(df)

        # Filter debits
        debits_df = df[df["Debit/Credit"] == "Debit"].copy()
        st.subheader("📊 Expenses")

        # Data editor with predictive suggestions
        def apply_predictions(row):
            if row["Category"] == "Uncategorized" and predictor:
                return suggest_category(row["Details"], predictor)
            return row["Category"]

        debits_df["Category"] = debits_df.apply(apply_predictions, axis=1)

        edited_df = st.data_editor(
            debits_df[["Date", "Details", "Amount", "Category"]],
            use_container_width=True,
            key="editor",
            hide_index=True
        )

        # Apply changes
        if st.button("💾 Save Changes"):
            for idx, row in edited_df.iterrows():
                new_category = row["Category"]
                details = row["Details"]
                debits_df.at[idx, "Category"] = new_category
                categories = add_keyword_to_category(categories, new_category, details)
            save_categories()
            save_session()
            st.success("Changes saved!")

        # Plots & analytics
        st.subheader("📈 Summary Charts")
        plot_category_pie(debits_df)
        plot_monthly_trend(debits_df)
        combined_chart(debits_df)
        top_vendors(debits_df)
        forecast_expenses(debits_df)

        # Budget alerts
        alerts = check_budget(debits_df)
        for alert in alerts:
            st.warning(alert)

        # Download updated CSV
        st.subheader("💾 Download Categorized Transactions")
        csv = debits_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV",
            data=csv,
            file_name="categorized_transactions.csv",
            mime="text/csv"
        )
