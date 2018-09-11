"""
https://www.youtube.com/watch?v=r_xb0vF1uMc

Summary:

find(): search for first matching result
find_all()/findAll(): Find all matching results
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'

res = requests.get(page)  # Build request
soup = BeautifulSoup(res.text, 'html.parser')  # Build parser
results = soup.find_all('span', attrs={'class':'short-desc'})

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')

"""
Notes:

results = soup.findAll('span', attrs={'class': 'short-desc'})
#len(results)  # Get count of results found
#results[0:3]  # Print the first 3 results
#results[-1]  # Check that the last result matches

# Extract date
first_result = results[0]  # Find the first result
first_result.find('strong')  # First strong tag
first_result.find('strong').text  # Text from first strong tag
first_result.find('strong').text[0:-1]  # Slice text from end of string
first_result.find('strong').text[0:-1] + ', 2017'  # Tag with date

# Extract the lie
first_result.contents  # Contents of first tag
first_result.contents[1]  # Extract second element
first_result.contents[1][1:-2]  # Remove curly quotes & space at the end.

# Extract explanation
first_result.contents[2]  # Explanation of lie
first_result.find('a')  #  Explanation by tag
first_result.find('a').text[1:-1]  # Text, minus open & close parentheses

# Extract URL
first_result.find('a')  # Link to proof in a tag
rint(first_result.find('a')['href']  # Link to proof URL

# Exporting as CSV
df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])  # Create dataframe
df.head()  # Examine top of dataframe
df.tail()  # Examine bottom of dataframe

df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime format
df.head()  # Head after datetime format
df.tail()  # Tail after datetime format

# Export to CSV
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
df = pd.read_csv('trump_lies.csv', parse_dates=['date'], encoding='utf-8')
"""