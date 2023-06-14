import vk_api
import course
import requests
from bs4 import BeautifulSoup

token = 'vk1.a.ASoyJpNAczmoMaOjjBRuMSz1GLDthT_YYEH6x5mw-4QgYSRxXcLZVY_95XUyZ3SbymeOM1HS3a8UHPEaycFKgB-RuD3k4vNAVyIxhniZZ53_x_FFUXo0Uw0M0mf-gtYBsR0ge54hZCUIgdVOkkxQDT7hoZIksHWCuG0Gar-3_WX7OCaKXR2oX4G_PfuSAt8fCIYIjYl99v707ngY3jxVgg'
vk = vk_api.VkApi(token=token)  # переменная для бота
vk._auth_token()


def largest_planet():  
    response = requests.get('https://swapi.dev/api/planets') 
    data = response.json() 
    largest = data['results'][0] 
    for planet in data['results']: 
        if int(planet['diameter']) > int(largest['diameter']): 
            largest = planet 
    return largest['name'] 

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

def get_starships(): 
    response = requests.get("https://swapi.dev/api/starships/") 
    starships = get_starships()["results"] 
    fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"])) 
    response = f'{fastest_starship["name"]}'   
    return response

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']  # текст сообщения от пользователя

        if message_text.lower() == 'курс доллара':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Курс доллара: {course.getCourse("R01235")}'})

        if message_text.lower() == 'планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Планета с максимальным диаметром: {largest_planet()}'})

        if message_text.lower() == "корабли":
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Самый быстрый корабль: {get_spaceships()}'})

        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

