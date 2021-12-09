from bs4 import BeautifulSoup
import requests,openpyxl

excel = openpyxl.Workbook()
sheet =excel.active
sheet.title ='Books'
sheet.append(['Title','Price','Availability'])


Html_data = requests.get('https://books.toscrape.com').text

soup = BeautifulSoup(Html_data,'lxml')

book_data = soup.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

for data in book_data:
    title = data.h3.a['title']
    price = data.find('p', class_='price_color').text[1:]
    stock = data.find('p',class_ = 'instock availability').text.strip()
    sheet.append([title,price,stock])
excel.save('Book details.xlsx')
