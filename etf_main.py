# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:24:19 2018

@author: SP
"""
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import datetime
import os
import etf_vnm
import etf_ftse
import etf_vfm
import etf_ssi
import dc
import pyn


def vofprice():
    page=requests.get('https://www.bloomberg.com/quote/VOF:LN')
    soup=html.fromstring(page.content)
    price=soup.xpath('//*[@id="content"]/div/div[1]/div[1]/div/div[4]/div[2]/text()')
    price=price[0]
    
    return(price)

def vofnav():
    page=requests.get('https://www.bloomberg.com/quote/VOF:LN')
    soup=html.fromstring(page.content)
    nav=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[8]/div[2]/text()')
    nav=nav[0]
    
    return(nav)

def vofspread():
    page=requests.get('https://www.bloomberg.com/quote/VOF:LN')
    soup=html.fromstring(page.content)
    spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[11]/div[2]/text()')
    spread=spread[0]
    return(spread)

def vofaum():
    page=requests.get('https://www.bloomberg.com/quote/VOF:LN')
    soup=html.fromstring(page.content)
    aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]/text()')
    aum=aum[0]
    return(aum)

print((datetime.datetime.now()), end='\n\n')
print('Giá ETF Vaneck hiện tại          : ', etf_vnm.priceVNM())  
print('Spread giữa giá ETF và NAV       : ', etf_vnm.spreadVNM())
print('Tổng AUM của VNM ETF USD mil     : ', etf_vnm.vnmaum(),'\n')

print('Giá của FTSE ETF (EUR)           : ', etf_ftse.ftseprice())
print('Spread giữa giá FTSE và NAV      : ', etf_ftse.ftsespread())
print('Tổng AUM của FTSE ETF EUR mil    : ', etf_ftse.ftseaum(),'\n')

print('Giá VFM VN30                     : ', etf_vfm.vfmprice())
print('Ngày chốt NAV                    : ', etf_vfm.vfmdate())
print('NAV của ETF VN30                 : ', etf_vfm.vfmnav())
print('AUM của ETF VFM VN30             : ', etf_vfm.vfmaum(),'\n')

p=etf_ssi.ssiprice()
print('Giá SSI ETF VN50                 : ', "%.0f"%p)
print('Ngày chốt NAV của ETF SSI VN50   : ', etf_ssi.ssidate())

n=etf_ssi.ssinav()
print('NAV gần nhất của SSI VN50        : ',n )
print('Tổng AUM của SSI VN50 VND bio    : ', etf_ssi.ssiaum())
print('Spread của SSI VN50              : ', etf_ssi.ssispread())

print()
print('Giá chứng chỉ VOF VinaCap        : ', vofprice())
print('NAV của chứng chỉ VOF            : ', vofnav())
print('Spread giá CCQ VOF và NAV        : ', vofspread())
print('AUM của VOF tỷ USD               : ', vofaum())

print()
page=requests.get('https://www.bloomberg.com/quote/VEIL:LN')
soup=html.fromstring(page.content)
price=soup.xpath('//*[@id="content"]/div/div[1]/div[1]/div/div[4]/div[2]/text()')
price=price[0]
nav=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[8]/div[2]/text()')
nav=nav[0]
spread=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[11]/div[2]/text()')
spread=spread[0]
aum=soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]/text()')
aum=aum[0]
print('Giá chứng chỉ quỹ VEIL (DC)      : ', price)
print('NAV của chứng chỉ VEIL           : ', nav)
print('Spread của chứng chỉ quỹ VEIL    : ', spread)
print('AUM của quỹ VEIL DC tỷ GBP       : ', aum)
print('Net cash của Quỹ VEIL %          : ', dc.netcash(),'%')

print()

print('Giá chứng chỉ quỹ PYN            : ', pyn.pynprice())
print('NAV của chứng chỉ PYN            : ', pyn.pynnav())
#print('Spread của chứng chỉ quỹ VEIL   : ', spread)
print('AUM của quỹ PYN triệu EUR        : ', pyn.pynaum())
#print('Net cash của Quỹ PYN %          : ', dc.netcash(),'%')

print()
print('Muốn lưu dữ liệu (y/n) ? ', end='')
yn=input()

if yn=='y':
    f=open("D:\\ETF data\\etf.txt", 'a')
    date=str(datetime.datetime.now())
    f.write(date)
    f.write('\n')
      
    pricevnm='USD'+ str(etf_vnm.priceVNM())
    spreadvnm=str(etf_vnm.spreadVNM())
    aumvnm=str(etf_vnm.vnmaum())
    
    f.write(pricevnm)
    f.write('    ')
    f.write(spreadvnm)
    f.write('    ')
    f.write(aumvnm)
    f.write('\n')
     
    priceftse=str(etf_ftse.ftseprice())
    spreadftse=str(etf_ftse.ftsespread())
    aumftse='EUR'+ str(etf_ftse.ftseaum())
   
    f.write(priceftse)
    f.write('     ')
    f.write(spreadftse)
    f.write('     ')
    f.write(aumftse)
    
    f.write('\n')
    f.write('Veil cash: ')
    f.write(dc.netcash())
    f.write('\n')
    f.close()