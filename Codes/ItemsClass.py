"""
-- detailed doc
-- check stat changes and prints
...
"""


class Items:
    """
    Common base for all items
    """

    def __init__(self, name):
        self.name = name

    def print_stat_change(self, max_hp, curr_hp, max_dmg, max_def, speed):
        if self.name == 'Potion':
            print("hp = " + curr_hp + " --> " + "hp = " + (curr_hp + 5))
        if self.name == "Recovery":
            print("hp = " + curr_hp + " --> " + "hp = " + max_hp)
        if self.name == "Medicinal Herb":
            print("hp = " + curr_hp + " --> " + "hp = " + (curr_hp + 2))
        # if self.name == "Holy Water":
        #     print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 2))
        #     print("Works only for a round")
        if self.name == "Copper Sword":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 3))
        if self.name == "Wooden Shield":
            print("def = " + max_def + " --> " + "def = " + (max_def + 2))
        if self.name == "Old Axe":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 4))
        if self.name == "Hunter's Axe":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 5))
        if self.name == "Rusted Shield":
            print("def = " + max_def + " --> " + "def = " + (max_def + 1))
        if self.name == "Iron Sword":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 8))
        if self.name == "Leather Shield":
            print("def = " + max_def + " --> " + "def = " + (max_def + 5))
            print("speed = " + speed + " --> "+ "speed = " + (speed - 1))
        if self.name == "Grand Axe":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 10))
            print("speed = " + speed + " --> " + "speed = " + (speed - 4))
        if self.name == "Standard Bow":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 3))
        if self.name == "Long Bow":
            print("dmg = " + max_dmg + " --> " + "dmg = " + (max_dmg + 6))
        if self.name == "Scale Shield":
            print("def = " + max_def + " --> " + "def = " + (max_def + 10))
            print("speed = " + speed + " --> " + "speed = " + (speed - 2))

    def stat_change(self, max_hp, curr_hp, max_dmg, max_def, speed):
        if self.name == 'Potion':
            return curr_hp + 5
        if self.name == "Recovery":
            return max_hp
        if self.name == "Medicinal Herb":
            return curr_hp + 2
        # if self.name == "Holy Water":
        #     return max_dmg * 2
        if self.name == "Copper Sword":
            return max_dmg + 3
        if self.name == "Wooden Shield":
            return max_def + 2
        if self.name == "Old Axe":
            return max_dmg + 4
        if self.name == "Hunter's Axe":
            return max_dmg + 5
        if self.name == "Rusted Shield":
            return max_def + 1
        if self.name == "Iron Sword":
            return max_dmg + 8
        if self.name == "Leather Shield":
            return max_def + 5 and speed - 1
        if self.name == "Grand Axe":
            return max_dmg + 10 and speed - 4
        if self.name == "Standard Bow":
            return max_dmg + 3
        if self.name == "Long Bow":
            return max_dmg + 6
        if self.name == "Scale Shield":
            return max_def + 10 and speed - 2

    def item_wielding_ability(self, race, curr_hp, max_hp):
        if self.name == "Potion" or self.name == "Recovery" or self.name == "Medicinal Herb":
            if curr_hp == max_hp:
                print("Your hp if full")
                return curr_hp

        if race == "Human":
            if self.name == "Old Axe" or self.name == "Hunter's Axe" or self.name == "Grand Axe":
                print("A Human cannot equip " + self.name)
                return False

        if race == "Dwarf":
            if self.name == "Copper Sword" or self.name == "Iron Sword" or self.name == "Standard Bow" \
                    or self.name == "Long Bow":
                print("Dwarves cannot equip " + self.name)
                return False

        if race == "Elf":
            if self.name == "Old Axe" or self.name == "Hunter's Axe" or self.name == "Grand Axe":
                print("Elves cannot equip " + self.name)
                return False

        if race == "Orc":
            if self.name == "Copper Sword" or self.name == "Iron Sword" or self.name == "Standard Bow" \
                    or self.name == "Long Bow":
                print("Orcs cannot equip " + self.name)
                return False

        return True
