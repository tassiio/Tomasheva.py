orders = int(input("Enter the amount of orders you have:\n"))
customers_dict = {}
orders_list = []
for i in range(orders):
    personal_order = input(f'{i+1} order: ')
    personal_order_lst = list(personal_order.split(sep=' '))
    name = personal_order_lst[0]
    pizza_type = personal_order_lst[1]
    amount = personal_order_lst[2]
    if name not in customers_dict:
        customers_dict[name] = {pizza_type: amount}
    else:
        if pizza_type not in customers_dict[name]:
            # customers_dict[name] |= {pizza_type: amount}
            customers_dict[name][pizza_type] = amount
        else:
            customers_dict[name][pizza_type] += amount

for name, orders in sorted(customers_dict.items()):
    print(f'{name}:')
    for pizza_type, amount in sorted(orders.items()):
        print('    ', pizza_type, amount)
