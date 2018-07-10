from ItemsClass import Items


class Character:

    """Character master class"""
    def __init__(self, base_speed, base_attack, base_defense, base_hp, race):

        self.base_speed = base_speed
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_hp = base_hp

        self.max_hp = base_hp

        self.current_speed = self.base_speed
        self.current_attack = self.base_attack
        self.current_defense = self.base_defense
        self.current_hp = self.max_hp
        self.alive = True
        self.damage = self.current_attack

        # init player coordinates
        self.x = 0
        self.y = 0

        self.key=False

        self.current_equipped_weapons = []
        self.item_list = []

        self.race = race

    # setters
    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    # getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_key(self):
        return self.key

    def die(self):
        if self.base_hp == 0:
            self.alive = False


    def consume_healing_item(self, given_item):
        if self.current_hp == given_item.item_wielding_ability(self.race, self.current_hp, self.base_hp):
            pass
        else:
            print(given_item.name, "consumed")
            self.item_list.append(given_item)
            self.current_hp = given_item.stat_change(self.max_hp, self.current_hp, self.damage, self.base_defense, self.current_speed)


    def change_stats(self, item):

        if item.name == "Potion" or item.name == "Recovery" or item.name == "Medicinal Herb":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_hp = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
            else:
                return False

        elif item.name == "Old Axe" or item.name == "Hunter's Axe" or item.name == "Grand Axe":
            if item.name == "Grand Axe":
                # if grand axe then two attributes changes (attack, speed)
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    attribute_list = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                    self.current_attack = attribute_list[0]
                    self.current_speed = attribute_list[1]
                    return True
                else:
                    return False
            else:
                # the other weapons ...
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    self.current_attack = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                    return True
                else:
                    return False

        elif item.name == "Copper Sword" or item.name == "Iron Sword" or item.name == "Standard Bow" or item.name == "Long Bow":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_attack = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                return True
            else:
                return False

        elif item.name == "Wooden Shield" or item.name == "Rusted Shield" or item.name == "Scale Shield" or item.name == "Leather Shield":
            if item.name == "Leather Shield" or item.name == "Scale Shield":
                # if grand axe then two attributes changes (attack, speed)
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):

                    attribute_list = item.stat_change(self.max_hp, self.current_hp, self.current_attack,
                                                      self.current_defense, self.current_speed)
                    self.current_attack = attribute_list[0]
                    self.current_speed = attribute_list[1]
                    return True
                else:
                    return False
            else:
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    self.current_defense = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                    return True
                else:
                    return False

    def add_item(self, item, starter_pack):
        # check if this weapon can be equipped
        if self.change_stats(item):
            if starter_pack:
                self.current_equipped_weapons.append(item)
            else:
                self.current_equipped_weapons.append(item)
                if "Axe" in item.name or "Sword" in item.name or "Bow" in item.name:
                    for i in self.current_equipped_weapons:
                        if "Axe" in i.name or "Sword" in i.name or "Bow" in i.name:
                            if self.change_stats(item):
                                self.current_equipped_weapons.append(item)
                                return self.current_equipped_weapons.pop(
                                    self.current_equipped_weapons.index(i))
                            else:
                                return False
        else:
            pass


class Dwarves(Character):

    def __init__(self, base_speed=20, base_attack=30, base_defense=30, base_hp=30, race="Dwarf"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)

        self.starter_pack_list = []

        self.items_Copper_Sword = Items("Copper Sword")
        self.items_Iron_Sword = Items("Iron Sword")
        self.items_Standard_Bow = Items("Standard Bow")
        self.items_Long_Bow = Items("Long Bow")

        self.items_Hunter_Axe = Items("Hunter's Axe")
        self.items_Wooden_Shield = Items("Wooden Shield")
        self.items_Potion = Items("Potion")

        self.items_Old_Axe = Items("Old axe")
        self.items_Rusted_Shield = Items("Rusted Shield")
        self.items_Medicinal_Herb = Items("Medicinal herb")

        self.items_Grand_Axe = Items("Grand axe")

        self.set_starter_pack()

    def set_starter_pack(self):

        self.starter_pack_list.append(self.items_Hunter_Axe)
        self.starter_pack_list.append(self.items_Wooden_Shield)


        self.starter_pack_list.append(self.items_Potion)
        # two potions included!
        self.starter_pack_list.append(self.items_Potion)

        # items_hunters_axe
        self.add_item(self.starter_pack_list[0], True)
        # items_wooden_shield
        self.add_item(self.starter_pack_list[1], True)
        # potion
        self.consume_healing_item(self.starter_pack_list[2])
        self.consume_healing_item(self.starter_pack_list[3])


class Orcs(Character):

    def __init__(self, base_speed=30, base_attack=35, base_defense=25, base_hp=35, race="orcs"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)

        self.starter_pack_list = []

        self.items_Copper_Sword = Items("Copper Sword")
        self.items_Iron_Sword = Items("Iron Sword")
        self.items_Standard_Bow = Items("Standard Bow")
        self.items_Long_Bow = Items("Long Bow")

        self.items_Hunter_Axe = Items("Hunter's axe")
        self.items_Wooden_Shield = Items("Wooden shield")
        self.items_Potion = Items("Potion")

        self.items_Old_Axe = Items("Old axe")
        self.items_Rusted_Shield = Items("Rusted shield")
        self.items_Medicinal_Herb = Items("Medicinal herb")

        self.items_Grand_Axe = Items("Grand axe")

        self.set_starter_pack()

    def set_starter_pack(self):
        self.starter_pack_list.append(self.items_Old_Axe)
        self.starter_pack_list.append(self.items_Rusted_Shield)
        self.starter_pack_list.append(self.items_Medicinal_Herb)
        self.starter_pack_list.append(self.items_Medicinal_Herb)
        self.starter_pack_list.append(self.items_Medicinal_Herb)


        self.add_item(self.starter_pack_list[0], True)
        self.add_item(self.starter_pack_list[1], True)

        self.consume_healing_item(self.starter_pack_list[2])
        self.consume_healing_item(self.starter_pack_list[3])
        self.consume_healing_item(self.starter_pack_list[4])