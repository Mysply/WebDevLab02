import streamlit as st
import pandas as pd
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Data Exploration - Bluey's Portfolio", page_icon="📊", layout="wide")

# --- PAGE HEADER ---
st.title("📊 Data Exploration with Bluey")
st.write("Explore interactive data visualizations and insights!")

# --- LOAD DATA FROM JSON ---
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"data": []}

data = load_data()
df = pd.DataFrame(data["data"])

# --- USER INPUT (INTERACTIVE ELEMENTS) ---
st.sidebar.header("🔧 Customize View")
selected_category = st.sidebar.selectbox("Select Category", df["category"].unique())  # NEW
filter_value = st.sidebar.slider("Filter Value", min_value=0, max_value=100, value=50)  # NEW

# --- FILTER DATA BASED ON USER INPUT ---
filtered_data = df[(df["category"] == selected_category) & (df["value"] >= filter_value)]

# --- DISPLAY DATA ---
st.subheader(f"Filtered Data: {selected_category}")
st.dataframe(filtered_data)  # NEW

# --- DATA VISUALIZATION ---
import matplotlib.pyplot as plt

st.subheader("📊 Static Data Visualization")
fig, ax = plt.subplots()
df.groupby("category")["value"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("📈 Dynamic Data Visualization")
fig2, ax2 = plt.subplots()
filtered_data.plot(x="subcategory", y="value", kind="line", ax=ax2)
st.pyplot(fig2)
