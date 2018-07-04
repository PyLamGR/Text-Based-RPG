import time

class Text:
    def __init__(self, body):
        self.body = body

    def show(self):
        print(self.body)

    def epic_read(self):
        for line in self.body.splitlines():
            time.sleep(2)
            print(line)

    def


fd = open("intro.txt", "r")
t1 = Text(fd.read())
t1.epic_read()