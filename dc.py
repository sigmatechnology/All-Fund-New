import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

def netcash():
    page=requests.get('http://portfolios.morningstar.com/fund/cef?t=VEIL&region=gbr&culture=en-US&ops=&cur=GBP&aaView=gbr&productcode=COM')
    soup=BeautifulSoup(page.content, 'html.parser')

    data=[]
    table=soup.find('table', {'id':'asset_allocation_tab'})
    rows=table.findAll('tr')

    for x, row in enumerate(rows[1:]):
        cols=row.findAll('td')
        for y,col in enumerate(cols):
            data.append([])
            data[x].append(col)

    cash=(data[2][3])
    cash=cash.text

    return cash