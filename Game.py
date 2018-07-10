import os

VERSION = 1.0
PATH = os.path.dirname(__file__)
menuItem = 0


def print_menu():
    print("|-----------------------------------------|")
    print("| 1) New Game                             |")
    print("| 2) Load game                            |")
    print("| 3) Help                                 |")
    print("| 4) About                                |")
    print("| 5) Exit                                 |")
    print("|-----------------------------------------|")


if __name__ == "__main__":
    print("PyLam THE GAME v.{0}".format(VERSION))
    print_menu()
