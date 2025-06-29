import requests 
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://ticker.finology.in/"
# url = "https://www.niftytrader.in/nse-option-chain"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

# Find the table with class 'table table-hover'
table = soup.find("table",class_ ="table table-sm table-hover screenertable")
header = table.find_all("th")


# insert all the data into the list
table_data  = table.find_all("tr")
table_actual = []
for i in table_data:
    table_actual.append(i.text)

# print(table_actual)

df = pd.DataFrame(table_actual)
print(df)
df.to_csv("stock.csv")


# insert all the company name into the list 
# company_name = table.find_all("a",class_="complink")
# company = []
# for i in company_name:
#     company.append(i.text)




# crteate a dataframe using pandas
# df = pd.DataFrame({"company":company})
# print(df)



# save into  csv file
# df.to_csv("company_detail.csv")