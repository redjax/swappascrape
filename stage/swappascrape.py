import requests
from bs4 import BeautifulSoup
import pandas as pd

page = 'https://swappa.com/buy/oneplus-5t-unlocked?storage=8'

res = requests.get(page)
soup = BeautifulSoup(res.text, 'html.parser')
result = soup.find('div', attrs={'class':'listing_previews'})
results = result.find_all('div', attrs={'class':'listing_row'})

records = []

for result in results:
    price = result.find('span', attrs={'class':'price'}).text
    # The seller name is in a span with no class, so build the div search first
    sellerdiv = result.find('div', attrs={'class':'seller_info'})
    seller = sellerdiv.find('span').text
    url = result.find('a')['href']  # Only gets the listing ID
    urlbuild = 'https://swappa.com' + url  # Build url with
    condition = result.find('span', attrs={'class':'condition_label'}).text
    color = result.find('span', attrs={'class':'color_label'}).text
    storage = result.find('span', attrs={'class':'storage_label'}).text
    records.append((price, seller, urlbuild, condition, color, storage))

df = pd.DataFrame(records, columns=['price', 'seller', 'url', 'condition', 'color', 'storage'])
df.to_csv('op5search.csv', index=False, encoding='utf-8')