""" Authored by: Aristos Karampelas Timotijevic"""

import time
import os
import pickle

"""
    こんばんわ!
    This is a python functionality elements collection!!
    GameTextClass: describes the texts that appear in the game.
    save & load: manage the processes save in a file and the reload in the game.
    
    For the save functions, the pickle module was used. Have fun checking the code.
"""


def save(file_name, player):
    """
        Explanation: Ask the user for a file name and also pass the player object in the function.
        The the code runs as such: It checks if the save_files dir already exists, and if it non-existent it
        creates it. Then it opens a file_desc for the file name given by the user.
    """

    if not os.path.exists("D:\\Text-Based-RPG\\Save_Files"):
        os.mkdir("D:\\Text-Based-RPG\\Save_Files", 0o777)
    with open("D:\\Text-Based-RPG\\Save_Files\\"+file_name+".bin", 'wb') as fd:
        print("Saving your Process...")
        pickle.Pickler(fd, 0).dump(player)
        print("Save complete!")


# the load function takes a save file and loads its contents


def load(file_name):
    """
        Explanation: This function takes a file_name as argument. The process is compromised by some additional checks.
        If the directory does not exist, then it will inform that a save must be done.
        If the directory does exist, but the demanded save file is non-existent, then it will inform the user
        accordingly. If all the upper checks are ok, then the save file will be loaded.
    """
    if not os.path.exists("D:\\Text-Based-RPG\\Save_Files"):
        print("No previous save data to be loaded!")
        return -1
    elif not os.path.exists("D:\\Text-Based-RPG\\Save_Files\\"+file_name+".bin"):
        print("File not Found!")
        return -1
    else:
        with open("D:\\Text-Based-RPG\\Save_Files\\"+file_name+".bin", 'rb') as fd:
            print("Now Loading...\('_')/")
            b = pickle.Unpickler(fd).load()
            print("Loading complete!")
            return b


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


class Dialogue(GameText):
    def __init__(self, file_name, actor):
        super(Dialogue, self).__init__(file_name)
        self.actor = actor

    def show_whole(self):
        with open(self.file_name, "r") as fd:
            print(self.actor+" : "+fd.read())


class Message(GameText):
    def __init__(self, file_name, event):
        super(Message, self).__init__(file_name)
        self.event = event
        print("Check on event")
        print("possible events: door, wall, room, enemy!")


if __name__ == "__main__":
    new = Story("intro.txt")
    new.epic_print()