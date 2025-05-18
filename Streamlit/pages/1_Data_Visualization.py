import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

# Load the data with caching
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'store.csv')  # Path to Streamlit/store.csv
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    file = pd.read_csv(file_path)
    # Sample up to 5000 rows, or all rows if fewer are available
    sample_size = min(5000, len(file))
    return file.sample(n=sample_size, random_state=42, replace=False)

# Load data
try:
    df = load_data()
    st.success(f"Dataset loaded successfully! ({len(df)} rows)")
except Exception as e:
    st.error(f"Error loading dataset: {str(e)}")
    st.stop()

# Title
st.title("📊 Data Exploration Dashboard")

# Sidebar Help Section
st.sidebar.header("📌 Visualization Help")
st.sidebar.info("""
This dashboard allows you to explore your data using:
- Scatter Plot
- Histogram
- Box Plot
- Correlation Heatmap
- Bar Chart
- Pie Chart

Use the controls to select columns and number of rows to display or analyze.
""")

# Display table controls
st.subheader("🔍 Data Table Viewer")
dis_rows = st.slider("Number of Rows", min_value=2, max_value=30, step=1)
dis_col = st.multiselect("Select Columns", df.columns.to_list(), default=df.columns.to_list())

if st.checkbox("📄 Show Data Table"):
    st.dataframe(df[dis_col].head(dis_rows))

# Identify column types
numerical_columns = df.select_dtypes(include=np.number).columns.to_list()
categorical_columns = df.select_dtypes(include='object').columns.to_list()
all_columns = df.columns.to_list()

# Ensure non-empty lists for visualizations
if not numerical_columns:
    st.warning("No numerical columns found. Some visualizations may be unavailable.")
    numerical_columns = all_columns[:1] if all_columns else []
if not categorical_columns:
    st.warning("No categorical columns found. Some visualizations may be unavailable.")
    categorical_columns = all_columns[:1] if all_columns else []

# Tabs for visualization types
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Scatter", "Histogram", "Box Plot", "Correlation Heatmap", "Bar Chart", "Pie Chart"])

# Scatter Plot
with tab1:
    st.header("🔹 Scatter Plot")
    x = st.selectbox("X Axis", numerical_columns, key='scatter_x')
    y = st.selectbox("Y Axis", numerical_columns, key='scatter_y')
    color = st.selectbox("Color By", all_columns, key='scatter_color')

    sampled_df = df.sample(n=min(1000, len(df)))  # Sample to improve performance
    scatter = px.scatter(sampled_df, x=x, y=y, color=color)
    st.plotly_chart(scatter, use_container_width=True)

# Histogram
with tab2:
    st.header("📊 Histogram")
    hist_col = st.selectbox("Select Column", numerical_columns, key='hist_col')
    hist = px.histogram(df, x=hist_col)
    st.plotly_chart(hist, use_container_width=True)

# Box Plot
with tab3:
    st.header("🧊 Box Plot")
    y = st.selectbox("Y Axis (numeric)", numerical_columns, key='box_y')
    x = st.selectbox("X Axis (categorical)", categorical_columns, key='box_x')
    box = px.box(df, x=x, y=y)
