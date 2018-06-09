import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

print('Danh mục của Vaneck ETF gần nhất: ')
res = requests.get('https://www.bloomberg.com/quote/VNM:US')
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )
