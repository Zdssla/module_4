import requests
from bs4 import BeautifulSoup as bs 
from datetime import datetime

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
response = requests.get(url+ f'date_reg={today} ')

xml = bs(response.content, features="xml")

def getCourse(id):
    return xml.find('Valute', {'ID':id}).Value.text.replace(',', '.')

'''print('На', today, '-', getCourse('R01235'), 'рублей за 1 доллар')
print('На', today, '-', getCourse('R01230'), 'рублей за 1 дирхам')
print('На', today, '-', getCourse('R01270'), 'рублей за 1 рупий')'''


'''n = int(input('Сколько долларов вам нужно? '))
print(f"За {n} долларов придется заплатить {int(n) * float(getCourse('R01235'))} рублей")'''

'''data = xml.find_all('Name')
for name in data:
    print(name.text)'''