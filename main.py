import streamlit as st
import pandas as pd
from pathlib import Path

# --- PATH SETUP ---
base_dir = Path(__file__).resolve().parent
DATA_FILENAME = "titanic.csv"
data_path = base_dir / DATA_FILENAME

st.title("🚢 Titanic Data Explorer")

# --- AUTO-DOWNLOAD REAL DATA ---
@st.cache_data
def get_real_data():
    url = "https://githubusercontent.com"
    data = pd.read_csv(url)
    data.to_csv(data_path, index=False) # Save it locally
    return data

# Check if we already have it; if not, get it
if not data_path.exists():
    with st.spinner("Downloading real data..."):
        df = get_real_data()
else:
    df = pd.read_csv(data_path)

# --- APP UI ---
st.success(f"Using local file: `{data_path.name}`")

st.subheader("Passenger Search")
search = st.text_input("Search by Name")
if search:
    df = df[df['Name'].str.contains(search, case=False)]

st.dataframe(df)

# Quick stat
st.metric("Survival Rate", f"{round(df['Survived'].mean() * 100, 1)}%")
