from Helpers.Door import Door
from Helpers.enemy import Goblin    # only goblins are in room1
from Helpers.Barrier import Barrier
from rooms.room1.subroom1 import subroom1Class

""" @Author: Sotiris Sapakos """

"""

 Help instructions
 -----------------------------------------
 
 X      = the player 
 O      = the enemies
 B      = Boss
 =      = The door
 ~      = barrier (cannot go through there)
 
 ------------------------------------------

"""

# table margins [21][21]
width = 21
height = 21

class room1:

    def __init__(self):
        self.room1Table = [[]]
        # player position variables
        self.playerPositionX = int(width / 2)
        self.playerPositionY = 0
        self.createRoom(width, height)

        self.baseKit = []

    def createRoom(self, width, height):
        # init game table as 2D matrix (is a simple list)
        self.room1Table = [[0 for i in range(width)] for j in range(height)]

        # empty table yet...
        for i in range(width):
            for j in range(height):
                self.room1Table[i][j] = " "

        # place player in room (and other components)
        self.placePlayerInTable(self.playerPositionX, self.playerPositionY)
        self.placeDoors()
        self.placeEnemies()
        self.placeBarriersNearDoor(self.door3)
        self.printRoom()

    def printRoom(self):
        # this is for better view of the game table
        helperLine = []
        for i in range(width + 2):
            helperLine.append("-")

        print(" ".join(helperLine))
        for i in range(width):
            print("|", " ".join(self.room1Table[i]), "|")

        print(" ".join(helperLine))
        pass

    # placement of all components
    def placePlayerInTable(self, X, Y):
        self.room1Table[X][Y] = "X"

    def placeDoors(self):
        # no need to get x or y coordinates as parameters
        # door1 = [0][12] - subroom1
        # door2 = [20][11] - subroom2
        # door3 = [8][20] - next basic room
        self.door1 = Door(0, 12)
        self.door2 = Door(20, 11)
        self.door3 = Door(8, 20)

        self.room1Table[self.door1.X][self.door1.Y] = "="

        self.room1Table[self.door2.X][self.door2.Y] = "="

        self.room1Table[self.door3.X][self.door3.Y] = "="

        pass

    def placeEnemies(self):
        # goblins in front of door that allows you to go to the next room!
        self.goblin1 = Goblin(8, 19)
        self.goblin2 = Goblin(9, 19)

        self.room1Table[self.goblin1.loc_x][self.goblin1.loc_y] = "O"
        self.room1Table[self.goblin2.loc_x][self.goblin2.loc_y] = "O"

    def placeBarriersNearDoor(self, door):
        # player cannot go to another room from the side of the door
        if door.X == width - 1 or door.X == 0:
            if door.X == 0:
                print("This room is subroom1")
            else:
                print("This door goes to subroom2")

            self.room1Table[door.X][door.Y - 1] = "~"
            self.room1Table[door.X][door.Y + 1] = "~"

        if door.Y == height - 1 or door.Y == 0:
            print("Especially this door is main room")
            self.room1Table[door.X-1][door.Y] = "~"
            self.room1Table[door.X+1][door.Y] = "~"
            # create new barriers to protection!
            self.barrier1 = Barrier(door.X-1, door.Y)
            self.barrier2 = Barrier(door.X+1, door.Y)

    # helper functions for better gaming!!
    def clearTable(self):
        print("\n" * 50)

    def checkAboutDoors(self, X, Y):
        if self.door1.checkEntry(X, Y) or self.door2.checkEntry(X, Y):
            # go to subrooms
            if self.door1.checkEntry(X, Y):
                # especially to subroom1
                print("Go especially to subroom1")
                subroom1 = subroom1Class.subroom1()
                print(self.baseKit)
            else:
                # especially to subroom2
                print("Go especially to subroom2")
                pass

        if self.door3.checkEntry(X, Y):
            # go to next room
            print("go into the other main room")
            pass
    def booleanCheckAboutDoors(self, X, Y):
        if self.door1.checkEntry(X, Y) or self.door2.checkEntry(X, Y) or self.door3.checkEntry(X, Y):
            return True
        return False

    def checkAboutEnemies(self, X, Y):
        if X == self.goblin1.loc_x and Y == self.goblin1.loc_y:
            print("Fall into an enemy...let's fight!")
            # 200 is a random number out of index of the gameTable
            # so as not to fight again with goblin 1
            self.goblin1.loc_x = 200
            self.goblin1.loc_y = 200
            pass
        if X == self.goblin2.loc_x and Y == self.goblin2.loc_y:
            print("Fall into an enemy...let's fight!")
            # maybe needs to check if player lives...
            self.goblin2.loc_x = 200
            self.goblin2.loc_y = 200
            pass

    def positionHasBarrier(self, X, Y):
        if self.barrier1.checkEntry(X, Y) or self.barrier2.checkEntry(X, Y):
            return True
        return False

    # player movement
    def goUp(self):
        if self.playerPositionX == 0:
            print("Cannot go further Up!")
        else:
            if self.positionHasBarrier(self.playerPositionX - 1, self.playerPositionY):
                print("Cannot go this way! Has barrier")
                return
            self.checkAboutDoors(self.playerPositionX - 1, self.playerPositionY)
            self.checkAboutEnemies(self.playerPositionX - 1, self.playerPositionY)

            # if there was a door behind player recreate it!
            if self.booleanCheckAboutDoors(self.playerPositionX, self.playerPositionY):
                self.room1Table[self.playerPositionX][self.playerPositionY] = "="
            else:
                self.room1Table[self.playerPositionX][self.playerPositionY] = " "

            self.playerPositionX = self.playerPositionX - 1
            self.placePlayerInTable(self.playerPositionX, self.playerPositionY)

        self.clearTable()
        self.printRoom()

    def goDown(self):
        if self.playerPositionX == height - 1:
            print("Cannot go further down!")
        else:
            if self.positionHasBarrier(self.playerPositionX + 1, self.playerPositionY):
                print("Cannot go this way! Has barrier")
                return

            self.checkAboutDoors(self.playerPositionX + 1, self.playerPositionY)
            self.checkAboutEnemies(self.playerPositionX + 1, self.playerPositionY)

            # if there was a door behind player recreate it!
            if self.booleanCheckAboutDoors(self.playerPositionX, self.playerPositionY):
                self.room1Table[self.playerPositionX][self.playerPositionY] = "="
            else:
                self.room1Table[self.playerPositionX][self.playerPositionY] = " "

            self.playerPositionX = self.playerPositionX + 1
            self.placePlayerInTable(self.playerPositionX, self.playerPositionY)

        self.clearTable()
        self.printRoom()

    def goLeft(self):
        if self.playerPositionY == 0:
            print("Cannot go further left!")
        else:
            # all ok...
            if self.positionHasBarrier(self.playerPositionX, self.playerPositionY - 1):
                print("Cannot go this way! Has barrier")
                return
            self.checkAboutDoors(self.playerPositionX, self.playerPositionY - 1)
            self.checkAboutEnemies(self.playerPositionX, self.playerPositionY - 1)

            # if there was a door behind player recreate it!
            if self.booleanCheckAboutDoors(self.playerPositionX, self.playerPositionY):
                self.room1Table[self.playerPositionX][self.playerPositionY] = "="
            else:
                self.room1Table[self.playerPositionX][self.playerPositionY] = " "

            self.playerPositionY = self.playerPositionY - 1
            self.placePlayerInTable(self.playerPositionX, self.playerPositionY)

        self.clearTable()
        self.printRoom()

    def goRight(self):
        if self.playerPositionY == width - 1:
            print("Cannot go further right!")
        else:
            if self.positionHasBarrier(self.playerPositionX, self.playerPositionY + 1):
                print("Cannot go this way! Has barrier")
                return
            self.checkAboutDoors(self.playerPositionX, self.playerPositionY + 1)
            self.checkAboutEnemies(self.playerPositionX, self.playerPositionY + 1)

            # if there was a door behind player recreate it!
            if self.booleanCheckAboutDoors(self.playerPositionX, self.playerPositionY):
                self.room1Table[self.playerPositionX][self.playerPositionY] = "="
            else:
                self.room1Table[self.playerPositionX][self.playerPositionY] = " "

            self.playerPositionY = self.playerPositionY + 1
            self.placePlayerInTable(self.playerPositionX, self.playerPositionY)

        self.clearTable()
        self.printRoom()