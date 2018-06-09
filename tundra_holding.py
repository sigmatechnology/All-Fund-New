import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html


def tundrafr():
    page = requests.get('https://www.bloomberg.com/quote/TUNDFRF:SS')
    soup = html.fromstring(page.content)
    ytd = soup.xpath('//*[@id="content"]/div/div[1]/div[1]/div/div[6]/div/div[4]/div[2]')
    ytd = ytd[0]
    ytd=ytd.text

    return ytd


def tundra_aum():
    page = requests.get('https://www.bloomberg.com/quote/TUNDFRF:SS')
    soup = html.fromstring(page.content)
    aum = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[2]')
    aum = aum[0]
    aum=aum.text

    return aum


def holding():

    print('Danh mục của Tundra gần nhất: ')
    res = requests.get('https://www.bloomberg.com/quote/TUNDFRF:SS')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))


print('YTD Performance Tundra Frontier Fund : ', tundrafr(),'%')
print('AUM của Tundra Frontier fund SEK Bil : ', tundra_aum())
print('Khoảng 240-250 mil USD')
print('TOP FUND HOLDINGS')
holding()
