import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html

def holding():

    res = requests.get('https://www.bloomberg.com/quote/VNH:LN')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

page=requests.get('https://www.bloomberg.com/quote/VNH:LN')

soup=html.fromstring(page.content)

spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[11]/div[2]')
spread=spread[0]
spread=spread.text
aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]')
aum=aum[0]
aum=aum.text


print('Spread của VIETNAM HOLDING       : ', spread)

print('AUM của quỹ VIETNAM HOLDING      : ', aum,'\n')
print('Danh mục của VIETNAM HOLDING     : ')

#print('Net cash của quỹ VEIL DC tỷ USD  : ', netcash())

holding()