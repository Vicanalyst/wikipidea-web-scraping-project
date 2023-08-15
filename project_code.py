#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_counties_of_Kenya_by_GDP'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the second table with the class 'wikitable sortable'
tables = soup.find_all('table', class_='wikitable sortable')
desired_table = tables[1]  # The second table

# Initialize empty lists to store data
data = {'Rank': [], 'County': [], 'GDP Per Capita (Kshs)': [], 'GDP Per Capita in US$ (PPP)': []}

# Iterate through the rows of the table
for row in desired_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) == 4:
        rank = columns[0].get_text(strip=True)
        county = columns[1].get_text(strip=True)
        gdp_kshs = columns[2].get_text(strip=True)
        gdp_usd_ppp = columns[3].get_text(strip=True)

        data['Rank'].append(rank)
        data['County'].append(county)
        data['GDP Per Capita (Kshs)'].append(gdp_kshs)
        data['GDP Per Capita in US$ (PPP)'].append(gdp_usd_ppp)

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Define the path for the CSV file
csv_path = r'C:\Users\User\Desktop\Projects\counties_by_gdp_per_capita.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_path, index=False)

print("DataFrame saved as CSV and stored in:", csv_path)


# In[2]:


df.head(10)

