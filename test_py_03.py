from unittest import TestCase
from py_03 import price_less_20


class TestPriceLess20(TestCase):
    def test_price_less20(self):
        items = {
            'milk15': {'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
            'cheese': {'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
            'sausage': {'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
        }
        self.assertEqual(price_less_20(items), { 'milk15': False, 'cheese': True, 'sausage': False})


