import time
import os
from .Game import PATH


def save():
    if not os.path.exists("save_data"):
        os.mkdir("save_data", 0o777)
    os.chdir("D:\\Text-Based-RPG\\save_data")
    fd = open("save", "wb")
    fd.write()


def load(file_name):
    os.chdir("D:\\Text-Based-RPG\\save_data")
    with open(file_name, "r") as fd:
        data = fd.read();
    return data


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