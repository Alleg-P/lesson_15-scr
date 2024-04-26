# Задача 2: Код-ревью для Романа

def Update_stock(item, quantity, stock):

    if item in stock:

        stock[item]['quantity'] += quantity

    else:

        stock[item] = {'quantity': quantity}


def get_Item_quantity(item_name, Stock):

    return Stock[item_name]['quantity']


def REMOVE_item(item, stock):

    if item in stock:

        del stock[item]


stock = {}


Update_stock('Apple', 50, stock)

Update_stock('Banana', 30, stock)

Update_stock('Coffee', 20, stock)


print(get_Item_quantity('Apple', stock))


REMOVE_item('Banana', stock)

print(stock)
