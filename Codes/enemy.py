import random
import ItemsList


class Enemy:

    def __init__(self, x, y):
        self.health = 15
        self.speed = 40
        self.attack = 20
        self.defence = 10
        self.loc_x = x
        self.loc_y = y
        self.alive = True
		self.name = "Goblin"
		
    def battle_player(self, x, y):
        # takes x, y parameters from player's location

        if self.loc_x <= x + 2 or self.loc_x >= x - 2 and self.loc_y <= y + 2 or self.loc_y >= y - 2:
            return True

    def attack_first(self, pl_speed):
        if self.speed > pl_speed:
            return True
        else:
            return False

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
		
		
        char_health -= max(hp_loss, 0)
		
        return char_health

    def defend(self):

        self.defence += 1

    def get_attacked(self, player_damage):
        damage = player_damage - self.defence
		
        self.health -= max(damage, 0)
        return


class Goblin(Enemy):
    # stats = [speed, attack, defence, health]
    stats = [40, 20, 10, 15]


    def battle_player(self, x, y):
        # takes x, y parameters from player's location

        if self.loc_x <= x + 1 or self.loc_x >= x - 1 and self.loc_y <= y + 1 or self.loc_y >= y - 1:
            return True

    @staticmethod
    def drop_item():

        # selects object from item list and returns it

        item_choice = random.randint(0, 1)      # 2 items to choose from

        if item_choice == 0:
            return ItemsList.potion    # potion
        elif item_choice == 1:
            return ItemsList.ws    # wooden shield

    def give_xp(self):
        if self.die() is True:
            self.exp = 10
            return self.exp


class Hobgoblin(Enemy):
    # stats = [speed, attack, defence, health]
    stats = [30, 22, 15, 20]

    def __init__(self, x, y):
        self.health = 20
        self.speed = 30
        self.attack = 22
        self.defence = 15
        self.loc_x = x
        self.loc_y = y
        self.alive = True
		self.name = "Hobgoblin"

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

    def give_xp(self):
        if self.die() is True:
            self.exp = 15
            return self.exp


class Bugbear(Enemy):
    # stats = [speed, attack, defence, health]
    stats = [10, 35, 20, 50]

    def __init__(self, x, y):
        self.health = 50
        self.speed = 10
        self.attack = 35
        self.defence = 20
        self.loc_x = x
        self.loc_y = y
        self.alive = True
		self.name = "Bugbear"

    @staticmethod
    def drop_item():

        # no need to choose....just returns treasure key
        # if true treasure key is returned

        return True

    def give_xp(self):
        if self.die() is True:
            self.exp = 20
            return self.exp
