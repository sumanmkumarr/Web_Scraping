import requests 
from bs4 import BeautifulSoup 
import pandas as pd

# lecture 13 

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")


# insert all the names of product into a list
names = soup.find_all("a",class_ ="title")
product_name = []
for i in names:
    name = i.text
    product_name.append(name)
print(product_name)



# insert all the prices of product into a list
product_price = []
prices = soup.find_all("h4",class_="price float-end card-title pull-right")
for i in prices:
    price = i.text 
    product_price.append(price)
print(product_price)


# insert all the description of product into a list
product_description = []
descs = soup.find_all("p",class_="description card-text")
for i in descs:
    desc = i.text
    product_description.append(desc)
print(product_description)



# insert all the review in a list
product_review = []
reviews = soup.find_all("p",class_="review-count float-end")
for i in reviews:
    review = i.text 
    product_review.append(review)
print(product_review)


# creating dataframe using pandas
df = pd.DataFrame({"product name":product_name,"product price":product_price,"product description":product_description,"product review":product_review})
print(df)

# saving the dataframe into a csv file
df.to_csv("product_detail.csv")

