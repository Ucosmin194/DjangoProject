from pprint import pprint

import bs4
import xlsxwriter
import requests
import datetime

url = 'https://www.emag.ro/desktop-pc/c?ref=hp_menu_quick-nav_23_1&type=category'
result = requests.get(url)  # verificam daca url este valid
soup = bs4.BeautifulSoup(result.text, 'lxml')  # bs ESTE UN PACHET PENTRU A ANALIZA DOCUMENTE HTML SI XML
cards = soup.find_all('div',
                      class_='card-v2')  # CAUTA DIV-URILE CARE CONTIN CLASA CARD-VR (ACESTE DIV-URI SUNT CARDURILE IN CARE ESTE PREZENTAT PRODUSUL
context = {'data': []}
for card in cards:  # PARCURGEM FIECARE CARD PENTRU A LUA NUMELE PRODUSULUI SI PRETUL
    data = {}
    product_name = card.find('a',
                             class_='card-v2-title semibold mrg-btm-xxs js-product-url')  # PRELUAM NUMELE PRODUSULUI
    product_price = card.find('p', class_='product-new-price')  # PRELUAM PRETUL
    if product_name is None:
        data['product_name'] = 'No data available'
    else:
        data['product_name'] = product_name.text

    if product_price is None:
        data['product_price'] = 'No data available'
    else:
        data['product_price'] = product_price.text

    context['data'].append(data)

workbook = xlsxwriter.Workbook('Desktop pc.xlsx')  # AM DEFINIT UN FISIERUL EXCEL
worksheet = workbook.add_worksheet('Desktop pc')  # AM DEFINIT UN SHEET IN FISIERUL EXCEL

row = 0
col = 0

for product in context['data']:
    worksheet.write(row, col, product['product_name'])  # AM SPECIFICAT PE PRIMA COLOANA SA FIE AFISAT NUMELE PRODUSULUI
    worksheet.write(row, col + 1, product['product_price'])  # AM SPECIFICAT PE A DOUA COLOANA PRETUL PRODUSULUI
    row += 1

workbook.close()