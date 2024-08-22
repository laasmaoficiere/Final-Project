import streamlit as st
import pickle
import numpy as np
import pandas as pd


# Load the trained model
with open('random_forest_model_final_1.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the CSV file containing the location data
location_data_df = pd.read_csv('Data/Unique_Neighborhoods.csv')

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



# Prepare the input array for prediction
input_features = np.array([[ minimum_nights, 
                            availability_365, room_type, 
                            neighborhood, city, state]])

df_no_outliers_encoded = pd.get_dummies(df_no_outliers, columns=['room_type', 'neighbourhood', 'city', 'state'], drop_first=True)

# Make a prediction
if st.button('Predict Price'):
    predicted_price = model.predict(input_features)
    st.write(f'The predicted price is: ${predicted_price[0]:.2f}')
