import requests
from bs4 import BeautifulSoup
from lxml import html
from tabulate import tabulate
import pandas as pd

def jpytd():
    page = requests.get('https://www.bloomberg.com/quote/JFVNOPP:HK')
    soup = html.fromstring(page.content)
    ytd = soup.xpath('//*[@id="content"]/div/div[1]/div[1]/div/div[6]/div/div[4]/div[2]')
    ytd = ytd[0]
    ytd=ytd.text

    return ytd


def jpaum():
    page = requests.get('https://www.bloomberg.com/quote/JFVNOPP:HK')
    soup = html.fromstring(page.content)
    aum = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[2]')
    aum = aum[0]
    aum=aum.text

    return aum

def holding():

    print('Danh mục của Vaneck ETF gần nhất: ')
    res = requests.get('https://www.bloomberg.com/quote/VNM:US')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

print('AUM của JP Morgan Vietnam Opportunities : ', jpaum())
print('Performance YTD của JPMorgan VN Opp     : ', jpytd(),'%')
holding()
