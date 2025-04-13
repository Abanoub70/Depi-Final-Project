# 🛒 Sales Forecasting and Optimization for E-commerce

This project focuses on developing a robust, production-ready **sales forecasting model** using real-world retail data. Leveraging historical sales data from Corporación Favorita (a major retailer), the project simulates an **e-commerce business scenario**, enabling insights into demand forecasting, inventory optimization, and promotional planning.

---

## 📌 Project Overview

**Goal:**  
To predict future sales at the product-store level using time-series forecasting models, and deploy the solution in a scalable, monitorable environment suitable for e-commerce operations.

**Key Components:**
- Data Collection & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Time-Series Forecasting Model Development
- Model Optimization
- MLOps: Deployment & Monitoring
- Final Documentation & Stakeholder Presentation

---

## 📂 Dataset Overview

The dataset used in this project is adapted from the [Favorita Grocery Sales Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting) competition on Kaggle.

| File                  | Description |
|-----------------------|-------------|
| `train.csv`           | Daily sales per item per store |
| `stores.csv`          | Metadata about each store (e.g., city, cluster) |
| `items.csv`           | Metadata about items (e.g., category, perishability) |
| `holidays_events.csv` | Local and national holidays and events |
| `transactions.csv`    | Daily transaction count per store |
| `oil.csv`             | Daily oil prices (macroeconomic factor) |

> 📝 **Note**: Although the data comes from physical stores, the modeling process simulates an e-commerce platform environment (e.g., stores as online warehouses, promotions as digital campaigns).

---

## 🧠 Problem Framing

- **Business Objective:** Improve inventory planning, promotional strategies, and sales forecasts to reduce overstocking/understocking in an e-commerce-like environment.
- **Forecasting Level:** Daily sales per item per store.
- **Time Series Features:** Seasonality, trends, promotions, holidays, transactions, economic indicators.

---

## 🔍 EDA Highlights

- Trend and seasonality detected at both global and product-store levels.
- Strong impact of holidays and promotions on sales spikes.
- Transaction volume is correlated with sales across stores.

---

## 🤖 Models & Techniques

- **Classical Models:** ARIMA, SARIMA
- **Machine Learning:** XGBoost, Random Forest Regressor
- **Deep Learning:** LSTM (experimental)
- **Hybrid Approaches:** Combining time-based features with regressor-based models

> 🔧 Model performance evaluated using:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

---

## ⚙️ Deployment & MLOps

- **Model Tracking:** MLflow
- **Version Control:** DVC
- **Deployment:** Flask or Streamlit API
- **Monitoring:** Logging metrics, model drift detection
- **Optional:** Cloud deployment on GCP/AWS/Heroku

---

## 📊 Interactive Dashboards

Developed using Plotly and Dash to visualize:
- Sales trends
- Seasonal spikes
- Store-level and item-level patterns
- Promotions and holidays impact

---

## 📁 Folder Structure

