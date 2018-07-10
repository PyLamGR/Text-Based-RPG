from Items import *
from helper import Position


class Character:
    name = "Unnamed Character"

    def __init__(self, base_speed, base_attack, base_defense, base_hp):
        self.current_speed = self.base_speed = base_speed
        self.current_attack = self.base_attack = base_attack
        self.current_defense = self.base_defense = base_defense
        self.current_hp = self.max_hp = self.base_hp = base_hp
        self.position = Position(0, 0)
        self.inventory = Inventory()

    def is_alive(self):
        """
        Check whether a player is alive or not.
        :return: True if the player is alive, false otherwise.
        """
        return self.current_hp > 0

    def kill(self):
        """
        Kills the character.
        :return:
        """
        self.current_hp = 0
        # TODO: Add something to actually kill the character.
        # TODO: Add drop items

    def __str__(self):
        return "{0}:\n" \
               " Speed   -> {1}\n" \
               " Attack  -> {2}\n" \
               " Defense -> {3}\n" \
               " HP      -> {4}\n".format(self.name, self.current_speed, self.current_attack,
                                          self.current_defense, self.current_hp)


