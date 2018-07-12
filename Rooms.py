from MapEntity import Door, Barrier, SpaceObject
from Characters.Enemies import Goblin, Hobgoblin, Bugbear


class Room:

    doors = []
    enemies = []
    barriers = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.room_table = [[SpaceObject(i, j) for i in range(width)] for j in range(height)]

    def create_room(self):
        """
        Generate/Create the room.
        """
        self.place_doors()
        self.place_enemies()
        self.print_room()

    def print_room(self):
        """
        Print the room as string for the user to see.
        """
        helper_line = []
        for i in range(self.width + 2):
            helper_line.append("-")

        print(" ".join(helper_line))

        for i in self.room_table:
            print("|", " ".join(map(str, i)), "|")

        print(" ".join(helper_line))

    def place_doors(self):
        """
        Automatically place the doors on the map.
        """
        for door in self.doors:
            self.room_table[door.position.x][door.position.y] = "="

    def place_enemies(self):
        """
        Automatically place the enemies on the map.
        """
        for enemy in self.enemies:
            self.room_table[enemy.position.x][enemy.position.y] = "O"  # TODO: place correct letters

    def place_barriers_near_door(self, door):

        """
        Automatically place the barriers near the given door on the map
        :param door: The door to place barriers
        """

        # in order to place the barriers at the correct position,
        # have to check if the given door
        # leads to another room or to a subroom
        if door.position.x == self.width-1 or door.position.x == 0:
            if door.position.x == 0:
                # this is subroom1 door...
                # TODO: add a class for subroom
                pass
            else:
                # this is subroom2 door...
                pass
            self.room_table[door.position.x][door.position.y - 1] = "~"
            self.room_table[door.position.x][door.position.y + 1] = "~"

            self.barriers.append(Barrier(door.position.x, door.position.y-1))
            self.barriers.append(Barrier(door.position.x, door.position.y+1))

        if door.position.y == self.height - 1 or door.position.y == 0:
            # this is next room door...
            self.room_table[door.position.x - 1][door.position.y] = "~"
            self.room_table[door.position.x + 1][door.position.y] = "~"

            self.barriers.append(Barrier(door.position.x-1, door.position.y))
            self.barriers.append(Barrier(door.position.x+1, door.position.y))


class Room1(Room):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.doors = [Door(0, 12),
                      Door(height-1, 11),
                      Door(10, width-1)]

        self.enemies = [Goblin(10, width-2),
                        Goblin(9, width-2)]

        self.place_barriers_near_door(self.doors[2])

        self.create_room()


class Room2(Room):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.doors = [Door(0, 12),
                      Door(height-1, 11),
                      Door(10, width-1)]

        self.enemies = [Goblin(1, 12),
                        Goblin(height-2, 11)]

        self.place_barriers_near_door(self.doors[0])
        self.place_barriers_near_door(self.doors[1])

        self.create_room()


class Room3(Room):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.doors = [Door(0, 12),
                      Door(height-1, 11),
                      Door(10, width-1)]

        self.enemies = [Hobgoblin(height-2, 11),
                        Bugbear(10, width-2)]

        self.place_barriers_near_door(self.doors[1])
        self.place_barriers_near_door(self.doors[2])

        self.create_room()
