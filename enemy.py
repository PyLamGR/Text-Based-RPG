import random


class Enemy:

    loc_x = 0
    loc_y = 0
    alive = True
    health = 0
    speed = 0
    attack = 0
    defence = 0
    exp = 0

    # maybe make it a dictionary?
    # size = 5 ?
    items = ["potion", "wooden shield", "iron sword", "iron shield", "treasure room key"]
    # need items objects (OBJECT LIST)       # give temporary strings

    def __init__(self, x, y):
        self.loc_x = x
        self.loc_y = y
        self.alive = True

    def battle_player(self, x, y):
        # takes x, y parameters from player's location

        if self.loc_x == x and self.loc_y == y:
            return True

    def die(self):

        # True if dead so the object can be deleted (maybe)

        if self.health == 0:
            self.alive = False
            return
        else:
            return

    @staticmethod
    def choose_action():            # if attack --> True    if defend --> False
        choice_rand = random.randint(0, 1)

        if choice_rand == 0:
            return True
        if choice_rand == 1:
            return False

    def attack_player(self, char_health, char_def):

        hp_loss = self.attack - char_def

        char_health -= hp_loss

        return char_health

    def defend(self):

        self.defence += 1


class Goblin(Enemy):

    health = 15
    speed = 40
    attack = 20
    defence = 10
    exp = 10

    def drop_item(self):

        # selects object from item list and returns it

        item_choice = random.randint(0, 1)      # 2 items to choose from

        if item_choice == 0:
            return self.items[0]    # potion
        elif item_choice == 1:
            return self.items[1]    # wooden shield


class Hobgoblin(Enemy):

    health = 20
    speed = 30
    attack = 22
    defence = 15
    exp = 15

    def drop_item(self):

        # selects object from item list and returns it

        item_choice = random.randint(0, 2)    # 3 items to choose from

        if item_choice == 0:
            return self.items[0]    # potion
        elif item_choice == 1:
            return self.items[2]    # iron sword
        elif item_choice == 2:
            return self.items[3]    # iron shield


class Bugbear(Enemy):

    health = 50
    speed = 10
    attack = 35
    defence = 20
    exp = 20

    def drop_item(self):

        # no need to choose....just returns treasure key

        return self.items[4]
