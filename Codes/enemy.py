import random
import ItemsList


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
    items = ["potion", "wooden shield", "iron sword", "iron shield", "treasure room key"]
    # maybe not needed

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

    def get_attacked(self, player_damage):
        damage = player_damage - self.defence
        self.health -= damage
        return


class Goblin(Enemy):

    health = 15
    speed = 40
    attack = 20
    defence = 10
    exp = 10

    @staticmethod
    def drop_item():

        # selects object from item list and returns it

        item_choice = random.randint(0, 1)      # 2 items to choose from

        if item_choice == 0:
            return ItemsList.potion    # potion
        elif item_choice == 1:
            return ItemsList.ws    # wooden shield


class Hobgoblin(Enemy):

    health = 20
    speed = 30
    attack = 22
    defence = 15
    exp = 15

    @staticmethod
    def drop_item():

        # selects object from item list and returns it

        item_choice = random.randint(0, 2)    # 3 items to choose from

        if item_choice == 0:
            return ItemsList.potion    # potion
        elif item_choice == 1:
            return ItemsList.irons    # iron sword
        elif item_choice == 2:
            return ItemsList.ss   # scale shield


class Bugbear(Enemy):

    health = 50
    speed = 10
    attack = 35
    defence = 20
    exp = 20

    @staticmethod
    def drop_item():

        # no need to choose....just returns treasure key
        # if true treasure key is returned

        return True
