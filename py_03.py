
items = {
    'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

def priceLess20(dict):
    d = {name: params['count'] < 20 for name, params in dict.items()}
    return d

print(priceLess20(items))