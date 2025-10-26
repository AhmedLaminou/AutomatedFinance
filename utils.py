import json
import streamlit as st

def load_categories(file="categories.json"):
    if "categories" not in st.session_state:
        st.session_state.categories = {"Uncategorized": []}
    try:
        with open(file, "r") as f:
            st.session_state.categories = json.load(f)
    except FileNotFoundError:
        pass
    return st.session_state.categories

def save_categories(file="categories.json"):
    with open(file, "w") as f:
        json.dump(st.session_state.categories, f, indent=2)

def save_session(file="session.json"):
    session_data = {
        "categories": st.session_state.categories,
        "budgets": st.session_state.budgets
    }
    with open(file, "w") as f:
        json.dump(session_data, f, indent=2)

def load_session(file="session.json"):
    try:
        with open(file, "r") as f:
            data = json.load(f)
        st.session_state.categories = data.get("categories", {"Uncategorized":[]})
        st.session_state.budgets = data.get("budgets", {})
    except FileNotFoundError:
        pass
