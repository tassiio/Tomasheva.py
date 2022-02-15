Kostya = int(input())
Owner = int(input())
print("Кубик Кости:", Kostya)
print("Кубик владельца:", Owner)
if Kostya > Owner:
    debt = (Kostya - Owner) * 1000
    print("Костя платит", debt, "долларов")
elif Kostya - Owner == 0:
    debt = 0
    print("Костя проиграл, но не платит")
else:
    debt = (Kostya + Owner) * 1000
    print("Владелец платит", debt, "долларов")
