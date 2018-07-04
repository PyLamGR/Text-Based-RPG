import sys

class mainScreen:

    gameVersion = 1.0
    menuItem = 0

    def __init__(self):
        self.printTitle()
        self.printMenu()
        self.menuItem = int(input("Choose an option(enter choice number): "))
        self.checkMenuItem(self.menuItem)
        pass

    def printTitle(self):
        print("PyLam THE GAME v." + str(self.gameVersion))

    @staticmethod
    def printMenu():
        print("|-----------------------------------------|")
        print("| 1) New Game                             |")
        print("| 2) Load game                            |")
        print("| 3) Help                                 |")
        print("| 4) About                                |")
        print("| 5) Exit                                 |")
        print("|-----------------------------------------|")

    @staticmethod
    def checkMenuItem(menuItem):
        if menuItem == 1:
            # new game started
            pass
        elif menuItem == 2:
            # load game started
            pass
        elif menuItem == 3:
            # help about the game
            pass
        elif menuItem == 4:
            # about our team
            pass
        else:
            # exit game
            print("Exit game!")
            sys.exit(0)