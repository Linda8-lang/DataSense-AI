## Import the necessary files
import pandas as pd
import streamlit as st
from groq import Groq
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(override=True)
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

# Page Setup
st.set_page_config(page_title="DataSense AI Copilot", page_icon="📊", layout="wide")

## the features
st.title("DataSense AI - Dataset & SQL Queries")
st.caption("Powered by GPT-OSS via Groq - 100% free open source")

# Sidebar for free Groq API Key
with st.sidebar:
    st.header("🔑 AI Setup")
    env_key = os.getenv("GROQ_API_KEY", "")
    if env_key:
        st.success("AI ready ✅")
        api_key = env_key
    else:
        api_key = st.text_input("Enter Free Groq API Key:", type="password")
    st.markdown("[Get a free key here (no credit card)](https://console.groq.com)")


# Data Loaders
def google_sheet_csv_url(url):
    """Turn a Google Sheets share link into its CSV export link."""
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9_-]+)", url)
    if not match:
        return None
    gid = re.search(r"[#&?]gid=(\d+)", url)
    export_url = f"https://docs.google.com/spreadsheets/d/{match.group(1)}/export?format=csv"
    if gid:
        export_url += f"&gid={gid.group(1)}"
    return export_url


@st.cache_data(show_spinner="Loading Google Sheet...")
def load_google_sheet(export_url):
    return pd.read_csv(export_url)


# Data Source Selection
source = st.radio("Data source", ["Upload a file (CSV / Excel)", "Google Sheets link"], horizontal=True)
df = None

if source == "Upload a file (CSV / Excel)":
    uploaded_file = st.file_uploader("Upload a CSV or Excel dataset", type=["csv", "xlsx", "xls"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.lower().endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                excel = pd.ExcelFile(uploaded_file)
                sheet = st.selectbox("Choose a sheet", excel.sheet_names) if len(excel.sheet_names) > 1 else excel.sheet_names[0]
                df = excel.parse(sheet)
        except Exception as e:
            st.error(f"Could not read the file: {e}")
else:
    sheet_url = st.text_input("Paste a Google Sheets link (shared as 'Anyone with the link can view'):")
    if sheet_url:
        export_url = google_sheet_csv_url(sheet_url)
        if not export_url:
            st.error("That doesn't look like a Google Sheets link.")
        else:
            try:
                df = load_google_sheet(export_url)
            except Exception as e:
                st.error(f"Could not load the Google Sheet. Make sure it is shared publicly. ({e})")

if df is not None:
    # 1. Exact Math Engine (Pandas)
    st.write("### 1. Dataset Preview")
    st.dataframe(df.head(5))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", int(df.isna().sum().sum()))

    # 2. User Question Input
    user_query = st.text_input("Ask a question or request a SQL query for this dataset:")

    if st.button("Generate AI Insights"):
        if not api_key:
            st.error("Please enter a free Groq API key in the sidebar to run the AI model.")
        elif not user_query:
            st.warning("Please type a question first.")
        else:
            # 3. Real LLM API Call
            client = Groq(api_key=api_key)
            schema = ", ".join(f"{col} ({dtype})" for col, dtype in df.dtypes.astype(str).items())
            prompt = f"""
You are an expert Data Analyst & SQL Engineer.
Table name: dataset
Dataset Columns (with types): {schema}
User Question: {user_query}

Provide:
1. A clear, 2-sentence plain-language summary answering the user question.
2. An optimized ANSI SQL query against the table `dataset` to extract this data.
"""
            with st.spinner("The AI is analyzing your dataset..."):
                try:
                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model=GROQ_MODEL,
                    )
                except Exception as e:
                    st.error(f"Groq API call failed: {e}")
                    st.stop()

            st.markdown("### 💡 AI Executive Summary & SQL")
            st.write(response.choices[0].message.content)
else:
    st.info("👆 Upload a CSV/Excel file or paste a Google Sheets link to test the copilot.")
