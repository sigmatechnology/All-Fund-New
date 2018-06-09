import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html

def holding():

    res = requests.get('https://vietnamphoenixfund.com/fund-allocation-and-performance/')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[4]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

    res = requests.get('https://vietnamphoenixfund.com/fund-allocation-and-performance/')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[2]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

page=requests.get('https://vietnamphoenixfund.com/general-shareholder-information/')

soup=html.fromstring(page.content)
aum=soup.xpath('//*[@id="tablepress-3"]/tbody/tr[3]/td[2]')
aum=aum[0]
aum=aum.text

page=requests.get('https://vietnamphoenixfund.com/fund-allocation-and-performance/')
soup=html.fromstring(page.content)
ngay=soup.xpath('/html/body/div[1]/div[3]/div/h3[4]/strong[2]')
ngay=ngay[0]
ngay=ngay.text

print('AUM của quỹ DWS            : ', aum,'\n')
print('Danh mục của DWS: ', ngay)

holding()

