import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def holding():
    print('Danh mục của VFM VF1 gần nhất: ')
    res = requests.get('https://vfm.com.vn/quy-dau-tu-chung-khoan-viet-nam-vfmvf1/vf1-danh-muc-dau-tu/')
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[4]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))


holding()

