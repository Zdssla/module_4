class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.weight + other.weight
        
    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
    
    def __mul__(self, other):
        if isinstance(other, Item):
            return self.weight * other.weight
        
    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        
item_1 = Item('Видеокарта', 85000, 1.2)
item_2 = Item('Процессор', 20000 , 0.3)

total_weight = item_1 + item_2 
difference_price = item_1 - item_2
production_weight = item_1 * item_2

div_price = item_1 / item_2

print(f'Общий вес комплектующих: {total_weight}кг.')
print(f'Разность цен комплектующих: {difference_price}руб.')
print(f'Произведение веса комплектующих: {production_weight}кг.')
print(f'Частное цен комплектующих: {div_price}руб.')