from rooms.room1.StartRoom_room1 import room1
from Helpers.CharacterClass import Character
from Helpers.Door import Door
from Helpers.enemy import Goblin    # only goblins are in room1
from Helpers.Barrier import Barrier
from rooms.room1.subroom1 import subroom1Class

# table margins [21][21]
width = 21
height = 21

class Room2:

    def __init__(self, object):
        # need to get the player from room1
        self.room2Table = [[]]
        self.createRoom(width, height)
        pass
    pass

    def createRoom(self, width, height):
        # init game table as 2D matrix (is a simple list)
        self.room2Table = [[0 for i in range(width)] for j in range(height)]

        # empty table yet...
        for i in range(width):
            for j in range(height):
                self.room2Table[i][j] = " "

        # place player in room (and other components)
        #self.placePlayerInTable(self.player.get_x(), self.player.get_y())
        self.placeDoors()
        self.placeEnemies()
        self.placeBarriersNearDoor(self.door2)
        self.placeBarriersNearDoor(self.door1)
        self.printRoom()

    def printRoom(self):
        # this is for better view of the game table
        helperLine = []
        for i in range(width + 2):
            helperLine.append("-")

        print(" ".join(helperLine))
        for i in range(width):
            print("|", " ".join(self.room2Table[i]), "|")

        print(" ".join(helperLine))
        pass

    # placement of all components
    def placePlayerInTable(self, X, Y):
        self.room2Table[X][Y] = "X"

    def placeDoors(self):
        # no need to get x or y coordinates as parameters
        # door1 = [0][6] - subroom3
        # door2 = [20][9] - subroom4
        # door3 = [11][20] - next basic room
        self.door1 = Door(0, 6)
        self.door2 = Door(20, 12)
        self.door3 = Door(11, 20)
        self.room2Table[self.door1.X][self.door1.Y] = "="
        self.room2Table[self.door2.X][self.door2.Y] = "="
        self.room2Table[self.door3.X][self.door3.Y] = "="
        pass

    def placeEnemies(self):
        # goblins in front of each subroom door
        self.goblin1 = Goblin(1, 6)
        self.goblin2 = Goblin(19, 12)
        self.room2Table[self.goblin1.loc_x][self.goblin1.loc_y] = "O"
        self.room2Table[self.goblin2.loc_x][self.goblin2.loc_y] = "O"

    def placeBarriersNearDoor(self, door):
        # player cannot go to another room from the side of the door
        if door.X == width - 1 or door.X == 0:
            if door.X == 0:
                pass
            else:
                pass
            self.room2Table[door.X][door.Y - 1] = "~"
            self.room2Table[door.X][door.Y + 1] = "~"
        if door.Y == height - 1 or door.Y == 0:
            self.room2Table[door.X - 1][door.Y] = "~"
            self.room2Table[door.X + 1][door.Y] = "~"
            # create new barriers to protection!
            self.barrier1 = Barrier(door.X - 1, door.Y)
            self.barrier2 = Barrier(door.X + 1, door.Y)

