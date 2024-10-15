
items = {
    'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

def price_less_20(dict):
    return {name: params['count'] < 20 for name, params in dict.items()}

if __name__ == '__main__':
    print(price_less_20(items))
