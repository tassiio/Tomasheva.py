import random


class Farmer:
    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        # print(type(self.garden))

    def take_care(self, which_potato, level_up):
        if not isinstance(which_potato, int) or not isinstance(level_up, int):
            raise ValueError
        self.garden[which_potato].ripeness += level_up

    def harvest(self):
        for i in range(len(self.garden)):
            if self.garden[i].ripeness >= 4:
                self.garden[i].ripeness -= 4
                print(f'Potato №{i} has been riped. The farmer has harvested.')


class Garden:
    def __init__(self, potatoes):
        self.potatoes = potatoes

    def get_info(self):
        return [[self.potatoes[i].position, self.potatoes[i].ripeness] for i in range(len(self.potatoes))]

    def growing(self):
        which_is_growing = random.choice([i for i in range(len(self.potatoes))])
        self.potatoes[which_is_growing].ripeness += 1
        for i in range(len(self.potatoes)):
            if self.potatoes[i].ripeness >= 4:
                print(f'Potato №{i} is ripe! Farmer should harvest!')


class Potato:
    def __init__(self, position, ripeness):
        self.position = position
        self.ripeness = ripeness

    def independent_growing(self):
        self.ripeness += 1
