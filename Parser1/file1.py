import lxml as lxml
import requests
from bs4 import BeautifulSoup

ssilka = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(ssilka)

soup = BeautifulSoup(response.text, 'lxml') # html.parser - помедленнее

data = soup.find_all('div', class_ = "col-lg-4 col-md-6 mb-4") # find позволяет получить содержимое тега.
# find_all - ищет все данные страницы

for i in data:
    name = i.find('h4', class_="card-title").text.replace('\n', '')
    price = i.find('h5').text
    url_img = "https://scrapingclub.com" + i.find('img', class_ = 'card-img-top img-fluid').get('src')# get позволяет получить содержимое атрибута

    print(name,'\n',price,'\n',url_img)