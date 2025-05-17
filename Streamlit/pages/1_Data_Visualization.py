import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load the data with caching
@st.cache_data
def load_data():
    file = pd.read_csv('store.csv')
    return file.sample(n=5000, random_state=42)


df = load_data()

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
    st.plotly_chart(box, use_container_width=True)

# Correlation Heatmap
with tab4:
    st.header("🔥 Correlation Heatmap")
    if len(numerical_columns) >= 2:
        corr_matrix = df[numerical_columns].corr()
        heatmap = px.imshow(
            corr_matrix,
            text_auto=True,
            color_continuous_scale='RdBu_r',
            title="Correlation Between Numerical Features"
        )
        st.plotly_chart(heatmap, use_container_width=True)
    else:
        st.warning("At least two numerical columns are required to show the heatmap.")

# Bar Chart
with tab5:
    st.header("📶 Bar Chart")
    cat_col = st.selectbox("Categorical Column", categorical_columns, key='bar_cat')
    num_col = st.selectbox("Numeric Column (for aggregation)", numerical_columns, key='bar_num')
    bar = px.bar(df, x=cat_col, y=num_col)
    st.plotly_chart(bar, use_container_width=True)

# Pie Chart
with tab6:
    st.header("🥧 Pie Chart")
    pie_cat = st.selectbox("Category Column", categorical_columns, key='pie_cat')
    pie_data = df[pie_cat].value_counts().reset_index()
    pie_data.columns = [pie_cat, 'Count']
    pie_chart = px.pie(pie_data, values='Count', names=pie_cat)
    st.plotly_chart(pie_chart, use_container_width=True)
