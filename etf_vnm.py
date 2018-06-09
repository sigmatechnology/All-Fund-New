# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:22:41 2018

@author: SP
"""
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import html

def priceVNM():
    page=requests.get('https://www.nasdaq.com/symbol/vnm/historical')
    soup=BeautifulSoup(page.content, 'html.parser')
    price_box=soup.find('div', attrs={'class':'qwidget-dollar'})
    price=price_box.text
    
    return price
    
def spreadVNM():
    page=requests.get('https://www.bloomberg.com/quote/VNM:US')
    soup=html.fromstring(page.content)
    spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[11]/div[2]/text()')
    spread=spread[0]
    #spread=spread.replace('%','')
    #spread=float(spread)
      
    return spread
   # spread=spread.strip('%')
 
def vnmaum():
    page=requests.get('http://www.etf.com/VNM')
    soup=html.fromstring(page.content)
    aum=soup.xpath('//*[@id="form-reports-overview"]/div[2]/div[1]/div/div[5]/span/text()')
    aum=aum[0]
    
    return aum