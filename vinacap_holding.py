import requests
from bs4 import BeautifulSoup
from lxml import html

def holding():
    page=requests.get('https://www.bloomberg.com/quote/VOF:LN')
    soup=BeautifulSoup(page.content, 'html.parser')

    data=[]
    table=soup.find('table', {'class':'data-table'})
    rows=table.findAll('tr')

    for x, row in enumerate(rows[1:]):
        cols=row.findAll('td')
        for y,col in enumerate(cols):
            data.append([])
            data[x].append(col)

    for i in range(10):
        for j in range(4):
            stock = data[i][j].text
            print(stock[0:10], end='   ')
        print()


holding()