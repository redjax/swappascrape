"""
Script created following tutorial here:
1. https://www.youtube.com/watch?v=0_VZ7NpVw1Y
2. https://www.youtube.com/watch?v=PI1-1TtFz50

The script is mostly from the second video, which teaches
scraping with the Wikipedia page for Machine Learning
(https://en.wikipedia.org/wiki/Machine_learning)
"""
import requests
import bs4

wikihead = '.mw-headline'  # Headline tag in Wikipedia.
wikicontents = '.toctext'

# The website to be scraped.
scrapesite = 'https://en.wikipedia.org/wiki/Machine_learning'

# Build the request variable
res = requests.get(scrapesite)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

soup.select(wikicontents)  # Select the tag.

# Get all headers
for i in soup.select(wikicontents):
    print(i.text)
