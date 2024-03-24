Netflix Data Analysis
Overview
This Python script analyzes a dataset of Netflix titles, providing insights into show and movie genres, countries of origin, ratings distribution, and more.
Prerequisites
Python 3.x
Pandas library
Seaborn library
Matplotlib library
Dataset
The script assumes a CSV file named "netflix_titles.csv" located in the same directory.
The expected columns in the dataset are:
title
director
cast
country
date_added
rating
duration
listed_in
type
Steps
Import Libraries: Imports necessary libraries for data analysis and visualization.
Load Dataset: Reads the CSV file into a DataFrame using Pandas.
Exploratory Analysis: Performs initial exploration of the data:
Describes the dataset's statistical summary.
Displays data types and memory usage.
Checks for missing values and handles them as needed.
Data Cleaning: Replaces missing values with "Unknown" for specified columns.
Visualizations: Generates visualizations using Seaborn and Matplotlib:
Shows the distribution of shows and movies by genre.
Displays the distribution of ratings.
Customizations: Allows for further exploration and analysis based on specific interests.
