from taxes_cl import *

your_money = float(input('Enter the amount of money you have: '))
your_apartment = Apartment(float(input('Enter the cost of your apartment: ')))
your_car = Car(float(input('Enter the cost of your car: ')))
your_country_house = CountryHouse(float(input('Enter the cost of your country house: ')))

tax = your_apartment.tax() + your_car.tax() + your_country_house.tax()
print(f'\nTaxes:\nApartment: {your_apartment.tax()}\nCar: {your_car.tax()}\nCountry house: {your_country_house.tax()}')
if your_money < tax:
    print("You don't have enough money to pay taxes.")
else:
    print("You have enough money to pay taxes.")
