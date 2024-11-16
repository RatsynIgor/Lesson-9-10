print('lesson 9: parsing of site')
import requests
from bs4 import BeautifulSoup
import sqlite3


data_site = requests.get('https://coinmarketcap.com/')
print('site coin market status code', data_site.status_code)

rates = []
if data_site.status_code == 200:
    print('coin market is connected')
    soup = BeautifulSoup(data_site.text, features="html.parser")
    soup_list = soup.find_all('div', {'class': 'sc-b3fc6b7-0 dzgUIj'})

    for block in soup_list:
        # print('parse', block)
        rate = float(block.findNext().text[1:].replace(',', ''))
        rates.append(rate)

print('value rates: ', rates)

sl3_connection = sqlite3.connect('crypto_ratesDB.sl3', 5)
sl3_cur =sl3_connection.cursor()

print('\nsl3 connection', sl3_connection)
print('cur', sl3_cur)

sl3_cur.execute('CREATE TABLE crypto_rates (print_date DATETIME, rate FLOAT)')

sl3_connection.close()