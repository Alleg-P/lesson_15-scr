# Задача 1: Исправление CRM-системы для магазина Романа

def add_client(name, history):
    client_id = len(history)+1
    history[client_id] = {'name': name, 'orders': []}

def make_order(client_id, history, order_details):
    history[client_id]['orders'].append(order_details)

def get_history(client_id, history):
    return history[client_id]['orders']

client_history: dict[str, int] = {}

add_client('Roman', client_history)

make_order(1, client_history, {'order_id': 1, 'amount': 100})

print(get_history(1, client_history))
