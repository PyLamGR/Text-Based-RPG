import GameTextClass as gtc

class Hero:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

h1 = Hero("Argibald")
gtc.save("h1", h1)

h2 = gtc.load("h2")
h2 = gtc.load("h1")
h1 = Hero("King Draco")
h1.show_name()
h2.show_name()
print(h2.name)
