Airbnb Data Analysis and Price Prediction
Overview
This project aims to explore and analyze Airbnb data for 10 major U.S. cities: Austin, Chicago, Columbus, Dallas, Denver, Los Angeles, New York, San Diego, San Francisco, and Seattle. The dataset includes information on Airbnb listings, including location, price, availability throughout the year, minimum nights, and reviews. The goal of this project is to provide insights into Airbnb pricing and review sentiments, as well as to build a price prediction model.

Cities Covered:
Austin
Chicago
Columbus
Dallas
Denver
Los Angeles
New York
San Diego
San Francisco
Seattle
Project Structure
Data: Contains the dataset used for analysis.
Scripts: Python scripts used for data analysis and model building.
Notebooks: Jupyter notebooks with detailed steps for data exploration, visualization, and model training.
Reports: Includes the final presentation and Tableau visualizations.
Exploratory Data Analysis (EDA)
Price Per Room/Accommodation Type
Analysis of how prices vary across different types of accommodations, such as entire homes/apartments, private rooms, shared rooms, and hotel rooms.
Price Per City
Comparison of average Airbnb prices across the 10 cities.
Identification of the most and least expensive cities in the dataset.
Availability and Minimum Nights
Exploration of Airbnb availability throughout the year and the minimum number of nights required for booking.
Review Analysis
Keyword Analysis
Extraction of the most common keywords in reviews to understand what guests value the most in their Airbnb experience.
Sentiment Analysis
Sentiment analysis of guest reviews to gauge the overall satisfaction level.
Visualization of sentiment distribution across different cities and room types.
Price Prediction Model
Model Description
A Random Forest Regressor was used to predict the price of an Airbnb listing based on the following features:
Room Type
Availability
Minimum Nights
Location (City, Neighborhood)
Model Performance
The model was evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) metrics.
Tableau Visualization
Explore interactive visualizations of the data, including:

Price distributions across cities and room types
Sentiment analysis by city and room type
Keyword frequency in guest reviews
Tableau Dashboard

Final Presentation
The final presentation includes the project overview, key findings, and model performance.

View Presentation

Getting Started
Prerequisites
Python 3.7+
Jupyter Notebook
pandas, numpy, scikit-learn, matplotlib, seaborn
Streamlit (for running the app)
Tableau Public (for visualizations)
Installation
Clone this repository to your local machine:

bash
Kopēt kodu
git clone https://github.com/yourusername/airbnb-analysis.git
Navigate to the project directory:

bash
Kopēt kodu
cd airbnb-analysis
Install the required packages:

bash
Kopēt kodu
pip install -r requirements.txt
Running the App
To run the Streamlit app for price prediction:

bash
Kopēt kodu
streamlit run app.py
Usage
Explore the Jupyter notebooks in the Notebooks directory to see the detailed analysis.
Use the Streamlit app to predict Airbnb prices based on selected features.
View the Tableau dashboard for interactive data visualizations.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The dataset used in this project is publicly available and was sourced from [source name, if applicable].
Special thanks to [your mentors, if applicable] for their guidance and support.
