list_food = ['burger', 'pasta', 'candy', 'kruttcapp', 'krabbypatty', 'Cheese', 'deeznuts', 'milkshake']
demand = input('enter a food: ')
demand = demand.lower()
list_food.sort()

def serving_food(list_food, demand):
    position = 0
    while position < len(list_food):
        if list_food[position] == demand:
            return f'{demand} is in the menu, going into your stomach within minutes'
        position += 1
    return f'{demand} is not in the menu'

print(serving_food(list_food, demand))