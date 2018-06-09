import requests
from bs4 import BeautifulSoup
from lxml import html

page=requests.get('https://www.bloomberg.com/quote/TUNDVIE:SS')
soup=BeautifulSoup(page.content, 'html.parser')

data=[]
table=soup.find('div', {'class':'change-container'})
print(table)

rows=table.findAll('::before')

print(rows)

