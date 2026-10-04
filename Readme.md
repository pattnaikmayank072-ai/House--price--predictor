# 🏠 California House Price Predictor

An interactive data science and machine learning web application built with [Streamlit](https://streamlit.io) that predicts median house values in California districts using an optimized [XGBoost Regressor](https://readthedocs.io) model.

## 🚀 Live Demo
*Coming soon! (Add your deployed Streamlit link here once live)*

## 📊 Project Overview
This project applies end-to-end machine learning workflows to predict real estate pricing trends based on 1990 US Census data from California block groups. It showcases how to successfully bridge an experimental exploratory data notebook into an elegant, consumer-facing software dashboard application.

### Key Highlights
* **High Predictive Power:** Achieved an R² score of **~0.947** on the training data matrices.
* **Modern UI:** Responsive split-column responsive user dashboard layout.
* **Production Ready Architecture:** Uses memory-efficient, uncorrupted native `.json` model loading framework instead of legacy standard pickle methods.

## 🛠️ Dataset Features & Architecture
The model relies on **8 core district features** parsed sequentially:
1. `MedInc`: Median income in block group (expressed in tens of thousands of USD).
2. `HouseAge`: Median house age within the block group block.
3. `AveRooms`: Average number of rooms per household.
4. `AveBedrms`: Average number of bedrooms per household.
5. `Population`: Total block group population.
6. `AveOccup`: Average number of household members.
7. `Latitude`: Block group geographic coordinate latitude.
8. `Longitude`: Block group geographic coordinate longitude.

## 💻 Local Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com
   cd california-house-price-predictor
   ```

2. **Install Required Software Dependencies**
   ```bash
   pip install streamlit pandas numpy xgboost scikit-learn
   ```

3. **Launch the Dashboard Application**
   ```bash
   streamlit run app.py
   ```

## 🏗️ Repository Architecture
```text
california-house-price-predictor/
├── app.py                     # Main Streamlit dashboard script application
├── house_model.json           # Trained native XGBoost regressor model weights 
├── README.md                  # Professional engineering documentation file
└── House_price_prediction.ipynb # Experimental exploratory data notebook profile
```