"""Script created by following tutorial here: https://www.youtube.com/watch?v=XQgXKtPSzUI"""

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

# Open connection and download page.
uClient = uReq(myurl)  # Download URL.
page_html = uClient.read() # Downloaded HTML.
uClient.close()  # Close the client after downloading.

# Parse HTML
pagesoup = soup(page_html, "html.parser")  # Parse the file as HTML.

# Grab each product
containers = pagesoup.findAll("div",{"class":"item-container"})
container = containers[0]
#print(container.div.div.a.img["title"])  # Item title example.

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", " | ") + "," + shipping + "\n")

    f.close()