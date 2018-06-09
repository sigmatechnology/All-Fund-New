# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:31:34 2018

@author: SP
"""
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import html

def ssiprice():
    page=requests.get('https://www.bloomberg.com/quote/FUESSV50:VN')
    soup=BeautifulSoup(page.content, 'html.parser')
    price_box=soup.find('div', attrs={'class': 'price'})
    price=price_box.text
    price=price.replace('.00','')
    
    price=price.replace(',','')
    
    price=float(price)
    return price

def ssidate():
    page=requests.get('https://www.bloomberg.com/quote/FUESSV50:VN')
    soup=html.fromstring(page.content)
    date=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[7]/div[1]/text()')
    date=date[0]
        
    return date
    
def ssinav():
    page=requests.get('https://www.bloomberg.com/quote/FUESSV50:VN')
    soup=html.fromstring(page.content)
    nav=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[5]/div[2]')
    nav=nav[0]
    nav=nav.text


    return nav

def ssispread():
    page=requests.get('https://www.bloomberg.com/quote/FUESSV50:VN')
    soup=html.fromstring(page.content)
    spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[8]/div[2]')
    spread=spread[0]
    spread=spread.text

    return spread

def ssiaum():
    page=requests.get('https://www.bloomberg.com/quote/FUESSV50:VN')
    soup=html.fromstring(page.content)
    aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[6]/div[2]')
    aum=aum[0]
    aum=aum.text
    return aum

