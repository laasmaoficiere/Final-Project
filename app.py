import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
with open('random_forest_model_final_1.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the CSV file containing the location data
location_data_df = pd.read_csv('Data/Cleaned_Airbnb_Data_No_Outliers.csv')

st.title('Airbnb Price Prediction App')

# Feature inputs
minimum_nights = st.number_input('Minimum Nights', min_value=1, max_value=365, value=2)
availability_365 = st.number_input('Availability 365', min_value=0, max_value=365, value=180)

# City and neighborhood selection
state = st.selectbox('State', location_data_df['state'].unique())

# Create city dataframe based on state selection
city_df = location_data_df[location_data_df['state'] == state]
city = st.selectbox('City', city_df['city'].unique())

# Create neighborhood dataframe based on city selection
neighborhood_df = city_df[city_df['city'] == city]
neighborhood = st.selectbox('Neighborhood', neighborhood_df['neighbourhood'])

# Room type selection
room_type = st.selectbox('Room Type', ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])

# Collect the input data into a DataFrame
input_data = pd.DataFrame({
    'minimum_nights': [minimum_nights],
    'availability_365': [availability_365],
    'state': [state],
    'city': [city],
    'neighbourhood': [neighborhood],
    'room_type': [room_type]
})

# Perform the same encoding as done during model training
encoded_input = pd.get_dummies(input_data, columns=['state', 'city', 'neighbourhood', 'room_type'], drop_first=True)

# Align the encoded input with the features expected by the model
# Ensure that all expected columns are present, fill missing ones with 0
for col in model.feature_names_in_:
    if col not in encoded_input.columns:
        encoded_input[col] = 0

# Remove any extra columns that are not expected by the model
encoded_input = encoded_input[model.feature_names_in_]

# Convert to numpy array for model prediction
input_features = encoded_input.values

# Make a prediction
if st.button('Predict Price'):
    predicted_price = model.predict(input_features)
    st.write(f'The predicted price is: ${predicted_price[0]:.2f}')
