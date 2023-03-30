/*


NYC Airbnb Data Analysis


*/

#1. Importing the Data
Context: Welcome to New York City (NYC), one of the most-visited cities in the world. 
As a result, there are many Airbnb listings to meet the high demand for temporary lodging for anywhere between a few nights to many months. 
In this notebook, we will take a look at the NYC Airbnb market by combining data from multiple file types like .csv, .tsv, and .xlsx.


Working with three datasets:

"datasets/airbnb_price.csv"

"datasets/airbnb_room_type.xlsx"

"datasets/airbnb_last_review.tsv"


Goals of project are to convert untidy data into appropriate formats to analyze, and answer key questions including:
- What is the average price, per night, of an Airbnb listing in NYC?
- How does the average price of an Airbnb listing, per month, compare to the private rental market?
- How many adverts are for private rooms?
- How do Airbnb listing prices compare across the five NYC boroughs?

import pandas as pd
import numpy as np
import datetime as dt

# Load airbnb_price.csv, prices
prices = ...

# Load airbnb_room_type.xlsx, xls
xls = pd.ExcelFile("...")

# Parse the first sheet from xls, room_types
room_types = ...

# Load airbnb_last_review.tsv, reviews
reviews = ...

# Print the first five rows of each DataFrame
print(prices.head(), "\n", room_types.head(), "\n", reviews.head())
