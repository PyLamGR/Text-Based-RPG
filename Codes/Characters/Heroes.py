import Items
from . import Character
from Items import Inventory
from helper import Position


class GenericHero(Character):
    name = "Generic Hero"

    def __init__(self, x, y, base_speed=40, base_attack=20, base_defense=10, base_hp=15):
        super().__init__(base_speed, base_attack, base_defense, base_hp)
        self.position = Position(x, y)
        self.inventory = Inventory()
        self.equipped_items = [None] * 2  # [0] -> Primary || [1] -> Secondary

        # Initial stats calculation
        self.calculate_stats()

    def modify_health(self, amount):
        """
        Modify the players health (Heal or damage)
        :param amount: Amount of health points to increase/decrease
        """
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        elif self.current_hp <= 0:
            pass  # TODO: Kill the Character

    def attack(self, other):
        pass

    def use_item(self, item: Items.Item):
        """
        Uses a specific item and removes it from the inventory
        :param item: Item to be used
        """
        if isinstance(item, Items.ItemHealing):
            self.modify_health(item.value)
            self.inventory.rem_item(item, 1)  # TODO: Remove item from inventory
        else:
            pass  # TODO: Check for other items that can be used from the inventory

    def calculate_stats(self):
        """
        Calculate attack and speed statistics for the hero.
        """
        for item in self.equipped_items:
            if item is None:
                continue
            if isinstance(item, Items.ItemAttack):
                self.current_attack += item.damage_modifier
                self.current_speed += item.speed_modifier
            elif isinstance(item, Items.ItemDefense):
                self.current_defense += item.defense_modifier
                self.current_speed += item.speed_modifier


class Human(GenericHero):
    name = "Human"

    def __init__(self, x, y):
        super().__init__(x, y, 30, 20, 15, 25)
        self.inventory.add_item(Items.HEALTH_POT, 2)
        self.equipped_items[0] = Items.COPPER_SWORD
        self.equipped_items[1] = Items.WOODEN_SHIELD
        self.calculate_stats()

class Elf(GenericHero):
    name = "Elf"

    def __init__(self, x, y):
        super().__init__(x, y, 35, 20, 10, 25)
        self.inventory.add_item(Items.HEALTH_POT)
        self.inventory.add_item(Items.MEDICAL_HERB, 2)
        self.equipped_items[0] = Items.STANDARD_BOW
        self.equipped_items[1] = Items.WOODEN_SHIELD
        self.calculate_stats()