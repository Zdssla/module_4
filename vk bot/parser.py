import requests
from pprint import pprint


url = 'https://swapi.dev/api/'

response = requests.get(url).json()


starhips_api = response.get('starships') # получение ссылки на космические корабли

def name_max_speed(url):
    """ Название самого быстрого космичесокго корабля."""
    
    speed_list = [] # список со скоростями кораблей
    name_list = [] # список названия кораблей
    for i in range(2, 11):
        response = requests.get(f'{url}/{i}').json() # запрос к сайту
        if response.get('name') is not None: # заполняем списки, если имя и скорость не None
            name_list.append(response.get('name'))
        if response.get('max_atmosphering_speed') is not None:
            speed_list.append(response.get('max_atmosphering_speed'))

    # находим максимальную скорость в списке speed_list
    max_speed = 0
    for speed in speed_list:
        if speed == 'n/a': # если нет данных по скорости, то пропускаем значение
            continue    
        if int(speed) > max_speed:
            max_speed = int(speed)
    
    # выводим на экран элемент списка name_list с тем же индексом, что индекс максимальной скорости в speed_list
    print(name_list[speed_list.index(str(max_speed))])

    
# вызов функции    
name_max_speed(starhips_api)