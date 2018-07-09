from rooms.room2.Room2 import Room2
from Helpers.CharacterClass import Character
from Helpers.Door import Door
from Helpers.enemy import Goblin, Hobgoblin, Bugbear    # only goblins are in room1
from Helpers.Barrier import Barrier
from rooms.room1.subroom1 import subroom1Class

# table margins [21][21]
width = 21
height = 21

class Room3:

    def __init__(self, object):
        # need to get the player from room1
        self.room3Table = [[]]
        self.createRoom(width, height)
        pass
    pass

    def createRoom(self, width, height):
        # init game table as 2D matrix (is a simple list)
        self.room3Table = [[0 for i in range(width)] for j in range(height)]

        # empty table yet...
        for i in range(width):
            for j in range(height):
                self.room3Table[i][j] = " "

        # place player in room (and other components)
        #self.placePlayerInTable(self.player.get_x(), self.player.get_y())
        self.placeDoors()
        self.placeEnemies()
        self.placeBarriersNearDoor(self.door2)
        self.placeBarriersNearDoor(self.door3)
        self.printRoom()

    def printRoom(self):
        # this is for better view of the game table
        helperLine = []
        for i in range(width + 2):
            helperLine.append("-")

        print(" ".join(helperLine))
        for i in range(width):
            print("|", " ".join(self.room3Table[i]), "|")

        print(" ".join(helperLine))
        pass

    # placement of all components
    def placePlayerInTable(self, X, Y):
        self.room3Table[X][Y] = "X"

    def placeDoors(self):
        # no need to get x or y coordinates as parameters
        # door1 = [0][6] - subroom5
        # door2 = [20][12] - subroom6
        # door3 = [10][20] - Treasure room door
        self.door1 = Door(0, 6)
        self.door2 = Door(20, 12)
        self.door3 = Door(10, 20)
        self.room3Table[self.door1.X][self.door1.Y] = "="
        self.room3Table[self.door2.X][self.door2.Y] = "="
        self.room3Table[self.door3.X][self.door3.Y] = "="
        pass

    def placeEnemies(self):
        # goblins in front of each subroom door
        self.goblin1 = Goblin(10, 18)
        self.hobgoblin = Hobgoblin(19, 12)
        self.boss = Bugbear(10,19)
        self.room3Table[self.goblin1.loc_x][self.goblin1.loc_y] = "O"
        self.room3Table[self.hobgoblin.loc_x][self.hobgoblin.loc_y] = "H"
        self.room3Table[self.boss.loc_x][self.boss.loc_y] = "B"

    def placeBarriersNearDoor(self, door):
        # player cannot go to another room from the side of the door
        if door.X == width - 1 or door.X == 0:
            if door.X == 0:
                pass
            else:
                pass
            self.room3Table[door.X][door.Y - 1] = "~"
            self.room3Table[door.X][door.Y + 1] = "~"
        if door.Y == height - 1 or door.Y == 0:
            self.room3Table[door.X - 1][door.Y] = "~"
            self.room3Table[door.X + 1][door.Y] = "~"
            # create new barriers to protection!
            self.barrier1 = Barrier(door.X - 1, door.Y)
            self.barrier2 = Barrier(door.X + 1, door.Y)

