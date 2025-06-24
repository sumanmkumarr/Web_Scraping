import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

url = "https://www.iplt20.com/auction" 

r = requests.get(url) 

# parse the HTML content using BeautifulSoup
# Use "lxml" parser for better performance
soup = BeautifulSoup(r.text,"lxml") 


# extract the whole table html 
table = soup.find("div",class_="tab-content",id="update_auction_data")
# print(table)

fund1 = table.find_all("div",class_="avg-fund-remaining")
# print(fund1)

fund = []
for i in fund1:
    fund.append(i.text.strip())

print(fund)