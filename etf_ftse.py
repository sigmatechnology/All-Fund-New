# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:29:55 2018

@author: SP
"""
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import html

def ftseprice():
    page=requests.get('https://www.bloomberg.com/quote/XFVT:GR')
    soup=BeautifulSoup(page.content, 'html.parser')
    price_box=soup.find('div', attrs={'class': 'price'})
    price=price_box.text
        
    return price
    
def ftsespread():    
    page=requests.get('https://www.bloomberg.com/quote/XFVT:GR')
    soup=html.fromstring(page.content)
    spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[11]/div[2]/text()')
    spread=spread[0]
    #spread=spread.replace('%','')
    #spread=float(spread)
    return spread

def ftseaum():
    page=requests.get('https://www.bloomberg.com/quote/XFVT:GR')
    soup=html.fromstring(page.content)
    aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]/text()')
    aum=aum[0]
    #spread=spread.replace('%','')
    #spread=float(spread)
    return aum