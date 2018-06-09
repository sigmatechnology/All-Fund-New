import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html

def holding():

    print('https://www.ishares.com/us/products/239649/ishares-msci-frontier-100-etf/1467271812596.ajax?fileType=csv&fileName=FM_holdings&dataType=fund')


#page=requests.get('https://www.ishares.com/us/products/239649/ishares-msci-frontier-100-etf#/')
#soup=BeautifulSoup(page.content, 'html.parser')
##name=soup.find('h1', attrs={'class': 'product-title'})
#name=name.text
#print(name)

holding()


