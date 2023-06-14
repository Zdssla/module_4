import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType 
import random 
import requests 
 
token = 'vk1.a.ASoyJpNAczmoMaOjjBRuMSz1GLDthT_YYEH6x5mw-4QgYSRxXcLZVY_95XUyZ3SbymeOM1HS3a8UHPEaycFKgB-RuD3k4vNAVyIxhniZZ53_x_FFUXo0Uw0M0mf-gtYBsR0ge54hZCUIgdVOkkxQDT7hoZIksHWCuG0Gar-3_WX7OCaKXR2oX4G_PfuSAt8fCIYIjYl99v707ngY3jxVgg' 
vk_session = vk_api.VkApi(token=token) 
vk = vk_session.get_api() 
longpoll = VkLongPoll(vk_session) 
 
def get_largest_planet(): 
    api_url = "https://swapi.dev/api/planets" 
    response = requests.get(api_url) 
    data = response.json() 
    largest = data["results"][0] 
    for planet in data["results"]: 
        if int(planet["diameter"]) > int(largest["diameter"]): 
          largest = planet 
    return largest["name"] 
 
for event in  longpoll.listen(): 
    if event.type == VkEventType.MESSAGE_NEW and event.to_me: 
        msg = event.text.lower() 
        user_id = event.user_id 
        random_id = random.randint(1,9999999) 
    if msg == "планеты": 
        response = f'{get_largest_planet()}' 
    else: 
        response = "Неизвестная команда" 
    vk.messages.send(peer_id = user_id, random_id = random_id, message=response)