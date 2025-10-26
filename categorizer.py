from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import streamlit as st

def categorize_transactions(df, categories):
    df["Category"] = "Uncategorized"
    
    for category, keywords in categories.items():
        if category == "Uncategorized" or not keywords:
            continue
        lowered_keywords = [k.lower().strip() for k in keywords]
        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            for kw in lowered_keywords:
                if fuzz.partial_ratio(details, kw) >= 80:  # Fuzzy match
                    df.at[idx, "Category"] = category
                    break
    return df

def add_keyword_to_category(categories, category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in categories[category]:
        categories[category].append(keyword)
    return categories

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


def train_predictor(df):
    df = df[df["Category"] != "Uncategorized"]
    if df.empty:
        return None
    X = df["Details"].values
    y = df["Category"].values
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)
    model = NearestNeighbors(n_neighbors=1, metric='cosine').fit(X_vec)
    return (model, vectorizer, X, y)

def suggest_category(detail, predictor):
    if predictor is None:
        return "Uncategorized"
    model, vectorizer, X_train, y_train = predictor
    vec = vectorizer.transform([detail])
    dist, idx = model.kneighbors(vec)
    return y_train[idx[0][0]]


