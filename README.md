# first_app_project
Sakila Data Analysis with Streamlit
Overview
This project uses Streamlit to perform data analysis on the Sakila dataset. The Sakila dataset is a sample database that represents a fictional DVD rental store. The analysis includes data cleaning, descriptive statistics, and visualizations to gain insights into the rental rates, return on investment, and other aspects of the dataset.

Getting Started
Prerequisites
Make sure you have the following Python libraries installed:

streamlit
pandas
numpy
matplotlib
seaborn
You can install them using:

bash
Copy code
pip install streamlit pandas numpy matplotlib seaborn
Running the App
To run the Streamlit app, execute the following command in your terminal:

bash
Copy code
streamlit run your_script_name.py
Replace your_script_name.py with the name of the Python script containing your Streamlit code.

Features
Data Overview:

Display basic information about the dataset.
Show the first and last rows of the dataset.
Data Cleaning:

Remove rows with missing values.
Descriptive Statistics:

Display descriptive statistics of the cleaned dataset.
Rental Rate Analysis:

Calculate the average rental rate.
Plot a density graph and a bar graph of rental rates.
Return on Investment Analysis:

Calculate and display the average and median rental gain return.
Plot a density graph of rental gain return with median and mean lines.
Maximal Replacement Cost:

Identify the film(s) with the maximum replacement cost.
Filter Films by Rating:

Allow users to filter films by selecting specific ratings ('PG' or 'PG-13').

