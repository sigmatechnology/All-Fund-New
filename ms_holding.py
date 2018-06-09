import requests
from bs4 import BeautifulSoup
from lxml import html


def jpytd():
    page = requests.get('http://portfolios.morningstar.com/fund/holdings?t=MFMIX&region=usa&culture=en-US')
    soup = html.fromstring(page.content)
    ytd = soup.xpath('//*[@id="content"]/div/div[1]/div[1]/div/div[6]/div/div[4]/div[2]')
    ytd = ytd[0]
    ytd=ytd.text

    return ytd


def jpaum():
    page = requests.get('http://portfolios.morningstar.com/fund/holdings?t=MFMIX&region=usa&culture=en-US')
    soup = html.fromstring(page.content)
    aum = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[2]')
    aum = aum[0]
    aum=aum.text

    return aum

def holding():
    page=requests.get('http://portfolios.morningstar.com/fund/holdings?t=MFMIX&region=usa&culture=en-US')
    soup=BeautifulSoup(page.content, 'html.parser')

    data=[]
    table=soup.findAll('tr')
    print(table)


#print('AUM của JP Morgan Vietnam Opportunities : ', jpaum())
#print('Performance YTD của JPMorgan VN Opp     : ', jpytd(),'%')
print('Top holding của Morgan Stanley Fund     : ')
holding()

