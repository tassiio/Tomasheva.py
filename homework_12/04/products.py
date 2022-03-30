goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key in goods:
    if key == 'Лампа':
        print(key, '-', store[goods[key]][0]["quantity"], "шт, ", "стоимость ",
              store[goods[key]][0]["quantity"] * store[goods[key]][0]["price"])
    elif key == 'Стол':
        print(key, '-', store[goods[key]][0]["quantity"] + store[goods[key]][1]["quantity"],
              "шт, ", "стоимость ", store[goods[key]][0]["quantity"] * store[goods[key]][0]["price"] +
              store[goods[key]][1]["quantity"] * store[goods[key]][1]["price"])
    elif key == 'Диван':
        print(key, '-', store[goods[key]][0]["quantity"] + store[goods[key]][1]["quantity"],
              "шт, ",
              "стоимость ", store[goods[key]][0]["quantity"] * store[goods[key]][0]["price"] +
              store[goods[key]][1]["quantity"] * store[goods[key]][1]["price"])
    else:
        print(key, '-', store[goods[key]][0]["quantity"] + store[goods[key]][1]["quantity"] +
              store[goods[key]][2]["quantity"], "шт, ",
              "стоимость ", store[goods[key]][0]["quantity"] * store[goods[key]][0]["price"] +
              store[goods[key]][1]["quantity"] * store[goods[key]][1]["price"] +
              store[goods[key]][2]["quantity"] * store[goods[key]][2]["price"])

