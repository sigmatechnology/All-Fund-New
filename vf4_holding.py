import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from lxml import html

def holding():
    print('Danh mục của VFM VF4 gần nhất: ')
    res = requests.get('https://vfm.com.vn/quy-dau-tu-doanh-nghiep-hang-dau-viet-nam-vfmvf4/vf4-danh-muc-dau-tu/')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[4]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

def aum():
    page = requests.get('https://www.bloomberg.com/quote/VFMVF4:VN')
    soup = html.fromstring(page.content)
    aum = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[2]')
    aum = aum[0]
    aum = aum.text

    soup = html.fromstring(page.content)
    ngay = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[1]')
    ngay=ngay[0]
    ngay=ngay.text

    print('AUM của VF4 : ', aum, 'vào ngày: ',ngay)
    print()

holding()
aum()
