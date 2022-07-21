from pprint import pprint

import bs4
import xlsxwriter
import requests
import datetime

url = 'https://www.flanco.ro/laptop-it-tablete/laptop.html'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
cards = soup.find_all('div', class_='product-item-info')
context = {'data': []}
for card in cards:
    data = {}
    product_name = card.find('a', class_='product-item-link')
    product_price = card.find('span', class_='price')
    if product_name is None:
        data['product_name'] = 'No data available'
    else:
        data['product_name'] = product_name.text

    if product_price is None:
        data['product_price'] = 'No data available'
    else:
        data['product_price'] = product_price.text

    context['data'].append(data)

workbook = xlsxwriter.Workbook('Laptop pc.xlsx')
worksheet = workbook.add_worksheet('Laptop pc')

row = 0
col = 0

for product in context['data']:
    worksheet.write(row, col, product['product_name'])
    worksheet.write(row, col + 1, product['product_price'])
    row += 1

workbook.close()

