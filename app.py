import streamlit as st
import xgboost as xgb
import numpy as np

# 1. Initialize and load your native XGBoost model
model = xgb.XGBRegressor()
model.load_model('house_model.json')

st.set_page_config(page_title="California House Price Predictor", page_icon="🏠", layout="centered")
st.title("🏠 California House Price Predictor")
st.write("Provide the neighborhood metrics below to calculate the estimated house value.")

# 2. UI Layout - Organizing fields into two columns to look professional
col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input("Median Income (in $10,000s)", min_value=0.5, max_value=15.0, value=3.5, step=0.1, help="Example: 3.5 = $35,000 yearly income")
    house_age = st.slider("Median House Age (Years)", min_value=1, max_value=52, value=28)
    ave_rooms = st.number_input("Average Rooms per House", min_value=1.0, max_value=10.0, value=5.4, step=0.1)
    ave_bedrms = st.number_input("Average Bedrooms per House", min_value=0.5, max_value=5.0, value=1.1, step=0.1)

with col2:
    population = st.number_input("Block Population", min_value=3, max_value=35000, value=1425, step=10)
    ave_occup = st.number_input("Average Household Occupancy", min_value=1.0, max_value=10.0, value=3.0, step=0.1)
    latitude = st.number_input("Location Latitude", min_value=32.0, max_value=42.0, value=35.6, step=0.01)
    longitude = st.number_input("Location Longitude", min_value=-124.0, max_value=-114.0, value=-119.5, step=0.01)

# 3. Predict Button Logic
if st.button("Estimate House Price", type="primary", use_container_width=True):
    # Construct array in the exact structure expected: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    features = np.array([[med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]])
    
    # Run the feature vector through your XGBoost model matrix
    raw_prediction = model.predict(features)
    
    # The California housing dataset target value is expressed in $100,000s.
    # Multiplying by 100,000 converts it back to standard currency format.
    final_price = float(raw_prediction[0]) * 100000
    
    if final_price < 0:
        st.error("⚠️ The input parameters represent highly improbable market combinations. Please adjust metrics.")
    else:
        st.success(f"💰 Estimated House Value: **${final_price:,.2f}**")