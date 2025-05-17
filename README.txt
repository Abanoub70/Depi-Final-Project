
Sales Prediction Model with Preprocessing Pipeline
==================================================

This project demonstrates how to build a machine learning pipeline that preprocesses both numerical and categorical features before applying a regression model. It uses a retail dataset that includes store details and sales data.

Project Structure
-----------------

data/
├── train.csv
└── store.csv

notebooks/
└── eda_and_modeling.ipynb

src/
└── preprocessing.py

models/
└── sales_model.pkl

README.txt
requirements.txt

Dataset
-------

- train.csv: Contains historical sales data for different stores.
- store.csv: Contains additional store-specific information.
Merged on the 'Store' column to create a single dataset.

Features Used
-------------

- Store, StoreType, Assortment
- CompetitionDistance, CompetitionOpenSinceMonth, CompetitionOpenSinceYear
- Promo2, Promo2SinceWeek, Promo2SinceYear, PromoInterval

Engineered Features:
- HasCompetition
- HasPromo2
- CompetitionTenure
- Promo_Jan to Promo_Dec
- StoreAge
- CompetitionDistanceCategory

Preprocessing Pipeline
----------------------

Built using sklearn.compose.ColumnTransformer and Pipeline. It consists of:

Numerical Features:
- Imputed with the column mean using SimpleImputer.

Categorical Features:
- Missing values filled with "Unknown" using SimpleImputer.
- One-hot encoded using OneHotEncoder with handle_unknown='ignore'.

Example:
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

Model
-----

After preprocessing, the transformed features are used to train a regression model to predict sales.

Example:
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

How to Run
----------

1. Clone this repo:
   git clone https://github.com/yourusername/sales-prediction-pipeline.git
   cd sales-prediction-pipeline

2. Install dependencies:
   pip install -r requirements.txt

3. Run the notebook or script to train the model:
   jupyter notebook notebooks/eda_and_modeling.ipynb

Requirements
------------

See requirements.txt for dependencies.

- pandas
- numpy
- scikit-learn
- matplotlib (optional for visualizations)

Future Improvements
-------------------

- Hyperparameter tuning
- Cross-validation
- Model explainability (e.g., SHAP)
- API for live predictions

Author
------

Abanoub Emad
LinkedIn: https://www.linkedin.com/
GitHub: https://github.com/
