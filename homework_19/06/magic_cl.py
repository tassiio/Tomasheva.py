class Water:
    answer = 'Water'

    def __add__(self, component):
        if isinstance(component, Air):
            return Storm()
        elif isinstance(component, Fire):
            return Steam()
        elif isinstance(component, Ground):
            return Dirt()
        elif isinstance(component, Water):
            return Water()


class Air:
    answer = 'Air'

    def __add__(self, component):
        if isinstance(component, Fire):
            return Lightning()
        elif isinstance(component, Ground):
            return Dust()
        elif isinstance(component, Water):
            return Storm()
        elif isinstance(component, Air):
            return Air()


class Fire:
    answer = 'Fire'

    def __add__(self, component):
        if isinstance(component, Ground):
            return Lava()
        elif isinstance(component, Water):
            return Steam()
        elif isinstance(component, Air):
            return Lightning()
        elif isinstance(component, Fire):
            return Fire()


class Ground:
    answer = 'Ground'

    def __add__(self, component):
        if isinstance(component, Water):
            return Dirt()
        elif isinstance(component, Air):
            return Dust()
        elif isinstance(component, Fire):
            return Lava()
        elif isinstance(component, Ground):
            return Ground()


class Lightning:
    answer = 'Lightning'


class Dust:
    answer = 'Dust'


class Storm:
    answer = 'Storm'


class Steam:
    answer = 'Steam'


class Dirt:
    answer = 'Dirt'


class Lava:
    answer = 'Lava'
