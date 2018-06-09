# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:10:14 2018

@author: SP
"""
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import html

def vfmprice():
    page=requests.get('https://www.bloomberg.com/quote/E1VFVN30:VN')
    soup=BeautifulSoup(page.content, 'html.parser')
    pricebox=soup.find('div', attrs={'class': 'price'})
    price=pricebox.text
    price=price.replace('.00','')
        
    return price
      
def vfmdate():
    page=requests.get('https://www.bloomberg.com/quote/E1VFVN30:VN')
    soup=html.fromstring(page.content)
    date=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[8]/div[1]')
    date=date[0]
    date=date.text
        
    return date
    
def vfmnav():
    page=requests.get('https://www.bloomberg.com/quote/E1VFVN30:VN')
    soup=html.fromstring(page.content)
    nav=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[8]/div[2]')
    nav=nav[0]
    nav=nav.text

    return nav

def vfmaum():
    page=requests.get('https://www.bloomberg.com/quote/E1VFVN30:VN')
    soup=html.fromstring(page.content)
    aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]')
    aum=aum[0]
    aum=aum.text
        
    return aum

