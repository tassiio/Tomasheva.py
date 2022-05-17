class Property:
    def __init__(self, worth: float):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth: float):
        if worth < 0:
            raise ValueError
        else:
            super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth: float):
        if worth < 0:
            raise ValueError
        else:
            super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth: float):
        if worth < 0:
            raise ValueError
        else:
            super().__init__(worth)

    def tax(self):
        return self.worth / 500
