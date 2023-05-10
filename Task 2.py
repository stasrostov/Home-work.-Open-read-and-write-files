from pprint import pprint
from collections import Counter

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dishes, person_count):
    dishes = sorted(dishes)
    shop_list = {}
    dish_count = Counter(dishes)
    for key, value in sorted(dish_count.items()):
        person_count *= value
        for dish_name, dish_ingridients in cook_book.items():
            if key == dish_name:
                for element in dish_ingridients:
                    for k, v in element.copy().items():
                        if k == 'quantity':
                            v *= person_count
                            element[k] = v
                        if k == 'ingredient_name':
                            popped_value = element.pop(k)
                            shop_list[popped_value] = element
    pprint(shop_list)


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 2)
