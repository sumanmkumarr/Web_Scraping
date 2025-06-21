import requests
from bs4 import BeautifulSoup

url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

# print(r.status_code)

# print(r.text)

soup = BeautifulSoup(r.text,"lxml")

# print(soup)

# tag = soup.div
# print(tag.attrs)

# tag2 = soup.div.p 
# print(tag2.string)


# find particular thing using tag name and class name 
t = soup.find("p",class_ ="description card-text")
print(t.string)