class Item:
    allowed_classes = []
    disallowed_classes = []

    def __init__(self, item_name="Unnamed Item"):
        self.item_name = item_name

    def __str__(self):
        return self.item_name


class ItemHealing(Item):
    def __init__(self, item_name, value):
        super().__init__(item_name)
        self.value = value


class ItemAttack(Item):
    def __init__(self, item_name, damage_modifier=0, speed_modifier=0):
        super().__init__(item_name)
        self.damage_modifier = damage_modifier
        self.speed_modifier = speed_modifier


class ItemDefense(Item):
    def __init__(self, item_name, defense_modifier=0, speed_modifier=0):
        super().__init__(item_name)
        self.defense_modifier = defense_modifier
        self.speed_modifier = speed_modifier


# TODO: Wielding ability

class Inventory:
    """
        Character inventory system.
        A user can interact with this inventory by adding or removing items
    """
    def __init__(self, size=-1):
        self.items = {}
        self.size = size

    def add_item(self, item: Item, amount: int = 1) -> bool:  # Check later
        pass

    def rem_item(self, item: Item, amount: int) -> bool:
        pass


# Medical Item
HEALTH_POT = ItemHealing("Health Potion", 5)
MEDICAL_HERB = ItemHealing("Medical Herb", 2)
RECOVERY = ItemHealing("Recovery", float("inf"))
HOLY_WATER = None  # SETUP Holly Water

# Swords
COPPER_SWORD = ItemAttack("Copper Sword", 3)
IRON_SWORD = ItemAttack("Iron Sword", 8)

# Shields
WOODEN_SHIELD = ItemDefense("Wooden Shield", 2)
RUSTED_SHIELD = ItemDefense("Rusted Shield", 1)
LEATHER_SHIELD = ItemDefense("Leather Shield", 5, -1)
SCALE_SHIELD = ItemDefense("Scale Shield", 10, -2)

# Axes
OLD_AXE = ItemAttack("Old Axe", 4)
HUNTERS_AXE = ItemAttack("Hunters Axe", 5)
GRAND_AXE = ItemAttack("Grand Axe", 10, -4)

# Bows
STANDARD_BOW = ItemAttack("Standard Bow", 3)
LONG_BOW = ItemAttack("Long Bow", 6)