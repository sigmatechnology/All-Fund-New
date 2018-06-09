import requests
from bs4 import BeautifulSoup
from lxml import html


def pynprice():
    page = requests.get('https://www.bloomberg.com/quote/ELITE:FH')
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find('div', {'class': 'price'})
    price = price.text

    return (price)


def pynnav():
    page = requests.get('https://www.bloomberg.com/quote/ELITE:FH')
    soup = html.fromstring(page.content)
    nav = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[9]/div[2]')
    nav = nav[0]
    nav = nav.text

    return (nav)


def pynaum():
    page = requests.get('https://www.bloomberg.com/quote/ELITE:FH')
    soup = html.fromstring(page.content)
    aum = soup.xpath('//*[@id="content"]/div/div[1]/div[8]/div/div/div[10]/div[2]')
    aum = aum[0]
    aum=aum.text
    return (aum)


print(pynnav)
print(pynaum)


