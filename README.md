# Airbnb Data Analysis and Price Prediction

## Overview

This project aims to explore and analyze Airbnb data for 10 major U.S. cities: Austin, Chicago, Columbus, Dallas, Denver, Los Angeles, New York, San Diego, San Francisco, and Seattle. The dataset includes information on Airbnb listings, including location, price, availability throughout the year, minimum nights, and reviews. The goal of this project is to provide insights into Airbnb pricing and review sentiments, as well as to build a price prediction model.

### Cities Covered:
- Austin
- Chicago
- Columbus
- Dallas
- Denver
- Los Angeles
- New York
- San Diego
- San Francisco
- Seattle

## Project Structure

- **Data:** Contains the dataset used for analysis.
- **Scripts:** Python scripts used for data analysis and model building.
- **Notebooks:** Jupyter notebooks with detailed steps for data exploration, visualization, and model training.
- **Reports:** Includes the final presentation and Tableau visualizations.

## Exploratory Data Analysis (EDA)

### Price Per Room/Accommodation Type
- Analysis of how prices vary across different types of accommodations, such as entire homes/apartments, private rooms, shared rooms, and hotel rooms.

### Price Per City
- Comparison of average Airbnb prices across the 10 cities.
- Identification of the most and least expensive cities in the dataset.

### Availability and Minimum Nights
- Exploration of Airbnb availability throughout the year and the minimum number of nights required for booking.

## Review Analysis

### Keyword Analysis
- Extraction of the most common keywords in reviews to understand what guests value the most in their Airbnb experience.

### Sentiment Analysis
- Sentiment analysis of guest reviews to gauge the overall satisfaction level.
- Visualization of sentiment distribution across different cities and room types.

## Price Prediction Model

### Model Description
- A Random Forest Regressor was used to predict the price of an Airbnb listing based on the following features:
  - Room Type
  - Availability
  - Minimum Nights
  - Location (City, Neighborhood)

### Model Performance
- The model was evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) metrics.

## Tableau Visualization

Explore interactive visualizations of the data, including:
- Price distributions across cities and room types
- Sentiment analysis by city and room type
- Keyword frequency in guest reviews

[Tableau Dashboard](https://public.tableau.com/app/profile/lasma.oficiere/viz/Book1_17243585527130/AirBnB?publish=yes)

## Final Presentation

The final presentation includes the project overview, key findings, and model performance.

**[View Presentation](#)**

## Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- pandas, numpy, scikit-learn, matplotlib, seaborn
- Streamlit (for running the app)
- Tableau Public (for visualizations)

## Streamlit App

A Streamlit app was developed to allow users to predict Airbnb prices based on selected features such as room type, availability, minimum nights, and location (city and neighborhood). The app dynamically filters neighborhoods based on the selected city, making it user-friendly even with a large number of neighborhood options.

### Running the App
To run the Streamlit app for price prediction:

```bash
streamlit run app.py

