import requests
from bs4 import BeautifulSoup
import dc
import pandas as pd
from tabulate import tabulate

def holding():
    print('Danh mục của DC VEIL gần nhất: ')
    res = requests.get('https://www.bloomberg.com/quote/VNM:US')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

print('Net cash danh mục VEIL: ', dc.netcash(),'%')
print('Danh mục của DC VEIL   : ')
holding()
