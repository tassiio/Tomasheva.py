from fun_farm import Farmer
from fun_farm import Garden
from fun_farm import Potato

potatoes = []
for i in range(5):
    potatoes.append(Potato(i, 0))
garden = Garden(potatoes)
farmer = Farmer('Jack', garden.potatoes)
print(garden.get_info())
farmer.take_care(0, 3)
print(garden.get_info())
farmer.take_care(0, 3)
print(garden.get_info())
farmer.harvest()
print(garden.get_info())
garden.growing()
garden.growing()
garden.growing()
garden.growing()

print(garden.get_info())
