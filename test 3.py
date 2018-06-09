import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html

res = requests.get('https://www.bloomberg.com/quote/9A311108:JP')
html = "div class=cell cell__mobile-basic cell__visible__even"

soup = BeautifulSoup(html, 'html.parser')

method1 = soup.find('div').text
method2 = soup.find('div').find('span').text
method3 = soup.find('span', class_='value-frame').text

print(method1)  # prints " whatever"
print(method2)
print(method3)
