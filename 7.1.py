from pprint import pprint

with open("recipes.txt", "r", encoding='utf-8-sig') as f:
    cook_book = {}

    while True:
        name = f.readline().rstrip()
        if not name:
            break
        number = int(f.readline().rstrip())
        ingredient = []
        for i in range(number):
            split_str = f.readline().rstrip().split(' | ')
            ingredient_list = {'ingredient_name': split_str[0],
                               'quantity': int(split_str[1]),
                               'measure': split_str[2]}
            ingredient.append(ingredient_list)
        f.readline()
        cook_book[name] = ingredient


def get_shop_list_by_dishes(dishes=[], person_count=0):
    list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            cook_book_dish = cook_book[dish]
            for i in cook_book_dish:
                quantity_i = 0
                if i['ingredient_name'] in list_by_dishes:
                    quantity_i = list_by_dishes[i['ingredient_name']]['quantity']
                list_by_dishes.update(
                    {i['ingredient_name']: {'measure': i['measure'],
                                            'quantity': quantity_i + i['quantity'] * person_count}
                     })
        else:
            print(f'Блюдо \'{dish}\' отсутствует, проверьте правильность ввода.')
    return list_by_dishes


pprint(get_shop_list_by_dishes(['Фахитос', 'Умлет'], 2))
