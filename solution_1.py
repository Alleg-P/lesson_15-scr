# Задача 1: Исправление CRM-системы для магазина Романа

def add_Client(name, history):
    client_id = len(history)+1
    history[client_id] = {'name': name, 'orders': []}


def Make_order(client_id, history, order_details):
    history[client_id]['orders'].append(order_details)


def GET_HISTORY(client_id, history):
    return history[client_id]['orders']


client_history = {}

add_Client('Roman', client_history)

Make_order(1, client_history, {'order_id': 1, 'amount': 100})

print(GET_HISTORY(1, client_history))
