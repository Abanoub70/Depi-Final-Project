import streamlit as st

with st.expander("📄 About Dataset", expanded=True):
    st.title("📊 Rossmann Store Sales Dataset Overview")

    st.markdown("""
    ### 📝 Dataset Description

    This dataset comes from the [Rossmann Store Sales Kaggle competition](https://www.kaggle.com/competitions/rossmann-store-sales), where participants were asked to forecast daily sales for over 1,000 Rossmann stores across Germany.

    Rossmann operates over 3,000 drug stores in several European countries. The dataset captures store-level information related to promotions, competition, and seasonality. It is designed to test time series forecasting, promotional analysis, and feature engineering skills.

    This dataset supports a wide range of analysis topics, including:
    - 📈 Sales forecasting
    - 📦 Promotion effectiveness
    - 🏪 Store segmentation
    - 🧭 Competitive landscape assessment

    """)

    st.markdown("### 📐 Dataset Dimensions")
    st.write("The dataset contains **1,115 rows** and **10 columns**, each representing information about a Rossmann store.")

    st.markdown("### 🧾 Column Descriptions")
    st.markdown("""
    - **Store** *(int)*: Unique identifier for each Rossmann store.
    - **StoreType** *(object)*: Encoded store type (e.g., a, b, c, d) indicating the business model.
    - **Assortment** *(object)*: Type of product assortment provided:
        - a = basic
        - b = extra
        - c = extended
    - **CompetitionDistance** *(float)*: Distance in meters to the nearest competitor store.
    - **CompetitionOpenSinceMonth** *(float)*: Month in which the nearest competitor opened.
    - **CompetitionOpenSinceYear** *(float)*: Year in which the nearest competitor opened.
    - **Promo2** *(int)*: Whether the store is running a continuous promotion (Promo2).
        - 0 = No
        - 1 = Yes
    - **Promo2SinceWeek** *(float)*: Calendar week when Promo2 started.
    - **Promo2SinceYear** *(float)*: Year when Promo2 started.
    - **PromoInterval** *(object)*: Months when Promo2 is active (e.g., "Jan,Apr,Jul,Oct").

    """)

    st.markdown("### ⚠️ Missing Values Summary")
    st.markdown("""
    Several columns contain missing values, especially those related to competition and promotions. Here's a summary:
    
    - `CompetitionDistance`: 3 missing
    - `CompetitionOpenSinceMonth`: 354 missing
    - `CompetitionOpenSinceYear`: 354 missing
    - `Promo2SinceWeek`: 544 missing
    - `Promo2SinceYear`: 544 missing
    - `PromoInterval`: 544 missing

    These missing values should be addressed during preprocessing (e.g., using imputation or assumptions).

    """)

    st.markdown("### 🔍 Why Is This Dataset Important?")
    st.markdown("""
    This dataset offers rich real-world features for business analysis. With it, you can:
    - 🧠 Build machine learning models to forecast store sales
    - 📊 Analyze the impact of promotional strategies like Promo2
    - 🌍 Understand how store location and distance to competition influence performance
    - 🔄 Perform time-series feature engineering with promotional calendar data
    """)

    st.markdown("### 💡 Analytical Tips")
    st.markdown("""
    - Combine this dataset with transactional sales data for full time-series modeling.
    - Encode categorical variables like `StoreType` and `Assortment`.
    - Use date features (e.g., year, month, week) when combined with daily sales data.
    - Evaluate if stores with active `Promo2` perform better, and how distance to competition correlates with sales.
    """)

    st.markdown("---")
    st.markdown("This expanded description helps readers and analysts quickly understand the scope and depth of the dataset for business forecasting and strategic insights.")

st.sidebar.header('ℹ️ About')
st.sidebar.info("""
- This tab provides a detailed explanation of the dataset used in this app.

- Explore data structure, feature meanings, missing values, and analytical insights.
""")
