import random
import Items

from . import Character
from helper import Position


class GenericEnemy(Character):
    name = "Generic Enemy"
    map_presence = "G"
    item_drops = []
    experience_points = 0

    def __init__(self, x, y, base_speed=40, base_attack=20, base_defense=10, base_hp=15):
        super().__init__(base_speed, base_attack, base_defense, base_hp)
        self.position = Position(x, y)

    @staticmethod
    def choose_action() -> bool:
        """
        Randomly chooses if the enemy will attack or defend.
        :return: True if an attack is performed, false otherwise.
        """
        return random.randint(0, 1) == 0

    def drop_item(self) -> Items.Item:
        """
        Randomly chooses an item to drop when the enemy is killed.
        :return: Random item from "item_drops" list if dead, none otherwise.
        """
        if self.is_alive():
            return None
        else:
            return random.randint(0, len(self.item_drops))


class Goblin(GenericEnemy):
    name = "Goblin"
    map_presence = "O"
    item_drops = [
        Items.HEALTH_POT,
        Items.WOODEN_SHIELD
    ]
    experience_points = 10

    def __init__(self, x, y):
        super().__init__(x, y, 40, 20, 10, 15)


class Hobgoblin(GenericEnemy):
    name = "Hobgoblin"
    map_presence = "H"
    item_drops = [
        Items.HEALTH_POT,
        Items.IRON_SWORD,
        Items.SCALE_SHIELD
    ]
    experience_points = 15

    def __init__(self, x, y):
        super().__init__(x, y, 30, 22, 15, 20)


class Bugbear(GenericEnemy):
    name = "Bugbear"
    map_presence = "B"
    item_drops = [
        Items.HEALTH_POT,
        Items.IRON_SWORD,
        Items.SCALE_SHIELD
    ]
    experience_points = 20

    def __init__(self, x, y):
        super().__init__(x, y, 10, 35, 20, 50)