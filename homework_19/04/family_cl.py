class Parent:
    def __init__(self, name, age, children):
        self.__name = name
        self.__age = age
        self.children = children

    def get_info(self):
        return [self.__name, self.__age, self.children]

    def calm(self, child):
        if child.name_ch in self.children:
            child.mood_ch = 'Good'
        else:
            print("This is a child of other parent.")

    def feed(self, child):
        if child.name_ch in self.children:
            child.hunger_ch = 'Wel-fed'
        else:
            print("This is a child of other parent.")

    def check(self, child):
        if self.__age - 16 > child.age_ch:
            print('Everything is okay.')

    def __str__(self):
        return self.__name + ', ' + str(self.__age) + ', ' + 'children:' + self.children


class Child:
    def __init__(self, name_ch, age_ch, mood_ch, hunger_ch):
        self.name_ch = name_ch
        self.age_ch = age_ch
        self.mood_ch = mood_ch
        self.hunger_ch = hunger_ch

    def __str__(self):
        return self.name_ch + ', ' + str(self.age_ch) + ', ' + self.mood_ch + ', ' + self.hunger_ch
