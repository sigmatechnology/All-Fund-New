import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html

def holding():
    res = requests.get(
        'http://www.trustnetoffshore.com/Factsheets/Factsheet.aspx?univ=DC&fundCode=DMFF9&pagetype=portfoliobreakdown')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.findAll('table')[9]

    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

def cash():
    page = requests.get(
        'http://www.trustnetoffshore.com/Factsheets/Factsheet.aspx?univ=DC&fundCode=DMFF9&pagetype=portfoliobreakdown')
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    table = soup.find('div', {'id': 'divAssetBox'})
    rows = table.findAll('tr')

    for x, row in enumerate(rows[1:]):
        cols = row.findAll('td')
        for y, col in enumerate(cols):
            data.append([])
            data[x].append(col)

    tienmat = data[2][3].text
    return tienmat

page=requests.get('http://www.trustnetoffshore.com/Factsheets/Factsheet.aspx?univ=DC&fundCode=DMFF9&pagetype=overview')

soup=html.fromstring(page.content)
aum=soup.xpath('//*[@id="boxContentBigLeft1"]/div[14]')
aum=aum[0]
aum=aum.text

print('AUM của quỹ PXP            : ', aum)
print('Tỉ lệ tiền mặt của PXP     : ', cash().rjust(15), '%')
print('Danh mục của PXP Vietnam Emerging Equity ')

holding()


