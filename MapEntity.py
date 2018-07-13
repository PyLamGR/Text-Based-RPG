from helper import Position


class MapEntity:
    map_presence = "M"

    def __init__(self, x, y):
        self.position = Position(x, y)

    def __str__(self):
        return self.map_presence


class Door(MapEntity):
    map_presence = "="

    def __init__(self, x, y):
        super().__init__(x, y)


class Barrier(MapEntity):
    map_presence = "~"

    def __init__(self, x, y):
        super().__init__(x, y)


class SpaceObject(MapEntity):
    map_presence = " "

    def __init__(self, x, y):
        super().__init__(x, y)

