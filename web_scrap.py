import requests
from bs4 import BeautifulSoup
import re

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
# t = soup.find("p",class_ ="description card-text")
# print(t.string)

# find all things of similar type using tag name and class name
# t2 = soup.find_all("p",class_="description card-text")
# print(len(t2))
# for i in t2:
#     print(i.string)



# find all using multiple tag name
# t3 = soup.find_all(["p","h4"])
# print(len(t3))
# for i in t3:
#     print(i.string)


# find all using string
# t4 = soup.find_all(string = "Prestigio SmartBook 133S Gold")
# print(t4)


#  find all using regex (regular expression)
# t5 = soup.find_all(string = re.compile("Prestigio"))
# print(t5)