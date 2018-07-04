""" Authored by: Aristos Karampelas Timotijevic"""

import time
import os

# functions for the text elements of the game

# save function takes an object and writes it in a binary file


def save():
    if not os.path.exists("save_data"):
        os.mkdir("save_data", 0o777)
    os.chdir("D:\\Text-Based-RPG\\save_data")
    fd = open("save", "wb")
    fd.write()
    print("saving")


# the load function takes a save file and loads its contents


def load():
    print("Loading...")


class GameText:

    def __init__(self, file_name):
        self.file_name = file_name

    def show_whole(self):
        with open(self.file_name, "r") as fd:
            print(fd.read())

    def show_to_line(self, limit):
        with open(self.file_name, "r") as fd:
            for i in range(limit):
                print(fd.readline().replace("\n", ""))

    def length(self):
        with open(self.file_name, "r") as fd:
            body = fd.read()
        return len(body)


class Story(GameText):
    def epic_print(self):
        with open(self.file_name, "r") as fd:
            for line in fd:
                time.sleep(1)
                print(line.replace("\n", ""))


if __name__ == "__main__":
    new = Story("welcome.txt")
    new.epic_print()