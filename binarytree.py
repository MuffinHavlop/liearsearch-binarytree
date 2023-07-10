list_food = ['burger', 'pasta', 'candy', 'kruttcapp', 'krabbypatty', 'Cheese', 'deeznuts', 'milkshake']
demand = input('enter a food: ')
demand = demand.lower()
list_food.sort()

def food_serve(list_food, demand):
    range = 0
    hi = len(list_food) - 1
    while range <= hi:
        mid = (range + hi)//2
        middle_food = list_food[mid]

        if middle_food == demand:
            return f"{demand} is in the menu, and will be in your stomach shortly"
        elif middle_food < demand:
            range = mid + 1
        elif middle_food > demand:
            hi = mid - 1
    return f'{demand} is not in the menu'

print(food_serve(list_food, demand))