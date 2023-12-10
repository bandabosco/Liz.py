import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


url = "https://www.amazon.com/s?k=electronics"


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = []
prices = []
ratings = []

for product in soup.find_all('div', {'data-component-type': 's-search-result'}):
    name = product.find('span', {'class': 'a-text-normal'})
    price = product.find('span', {'class': 'a-offscreen'})
    rating = product.find('span', {'class': 'a-icon-alt'})

    if name and price:
        products.append(name.text.strip())
        prices.append(price.text.strip())
    else:
        continue

    if rating:
        ratings.append(float(rating.text.split()[1]))
    else:
        ratings.append(None)


df = pd.DataFrame({'Product': products, 'Price': prices, 'Rating': ratings})
print(df.to_string)

plt.figure(figsize=(10, 6))
plt.scatter(df['Rating'], df['Price'])
plt.xlabel('Rating')
plt.ylabel('Price')
plt.title('Rating against Price for Electronics')
plt.show()