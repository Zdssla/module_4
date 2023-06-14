from pprint import pprint

if __name__ == '__main__':
    goods = [
        {
            'name': 'iphone 14',
            'brand': 'Apple',
            'price': 1200
        },
        {
            'name': 'Samsung Galaxy A50',
            'brand': 'Samsung',
            'price': 600
        },
        {
            'name': 'Xiaomi Mi 10T',
            'brand': 'Xiaomi',
            'price': 400
        },
    ]

    #def item_price(item):
    #   return item['price']
        
    #pprint(sorted(goods, key=lambda item: item['price']))

    # все товары юренда Apple
    apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
    #print(apple_list) 

    # функция map
    numbers = ['1', '2', '3', '4', '5']
    numbers = list(map(int, numbers))
    #print(numbers)

    names = ['Slava', 'John', 'Bob']
    surnames = ['Zhirov', 'Jones', 'Stroitel']

    full_names = list(map(lambda name, surname: f'{name} {surname}', names, surnames))
    #print(full_names)

    # функция enumerate
    indexed_doods = []
    for index, item in enumerate(goods):
        indexed_doods.append({index: item})
    #print(indexed_doods)

    # функция zip
    patronymics = ['Denisovich', 'Joneson', 'Bober']
    for name, surname, patronymics in zip(names, surnames, patronymics):
        print(surname, name, patronymics)
