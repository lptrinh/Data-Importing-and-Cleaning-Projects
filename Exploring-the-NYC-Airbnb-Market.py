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
prices = pd.read_csv("datasets/airbnb_price.csv")

# Load airbnb_room_type.xlsx, xls
xls = pd.ExcelFile("datasets/airbnb_room_type.xlsx")

# Parse the first sheet from xls, room_types
room_types = xls.parse(0)

# Load airbnb_last_review.tsv, reviews
reviews = pd.read_csv("datasets/airbnb_last_review.tsv", sep="\t")

# Print the first five rows of each DataFrame
print(
  prices.head(), 
  "\n", 
  room_types.head(), 
   "\n", 
  reviews.head()
)

   listing_id        price                nbhood_full
0        2595  225 dollars         Manhattan, Midtown
1        3831   89 dollars     Brooklyn, Clinton Hill
2        5099  200 dollars     Manhattan, Murray Hill
3        5178   79 dollars  Manhattan, Hell's Kitchen
4        5238  150 dollars       Manhattan, Chinatown 

    listing_id                                description        room_type
0        2595                      Skylit Midtown Castle  Entire home/apt
1        3831            Cozy Entire Floor of Brownstone  Entire home/apt
2        5099  Large Cozy 1 BR Apartment In Midtown East  Entire home/apt
3        5178            Large Furnished Room Near B'way     private room
4        5238         Cute & Cozy Lower East Side 1 bdrm  Entire home/apt 

    listing_id    host_name   last_review
0        2595     Jennifer   May 21 2019
1        3831  LisaRoxanne  July 05 2019
2        5099        Chris  June 22 2019
3        5178     Shunichi  June 24 2019
4        5238          Ben  June 09 2019

#2. Cleaning the price column
DataFrames have been loaded, first step is to calculate the average price per listing by room_type.
You may have noticed that the price column in the prices DataFrame currently states each value as a string with the currency (dollars) following, i.e.,

  price
  225 dollars
  89 dollars
  200 dollars
  
We will need to clean the column in order to calculate the average price.

# Remove whitespace and string characters from prices column
prices["price"] = prices["price"].str.replace(" dollars"," ")

# Convert prices column to numeric datatype
prices["price"] = pd.to_numeric(prices["price"])

# Print descriptive statistics for the price column
print(prices["price"].describe())


count    25209.000000
mean       141.777936
std        147.349137
min          0.000000
25%         69.000000
50%        105.000000
75%        175.000000
max       7500.000000
Name: price, dtype: float64


