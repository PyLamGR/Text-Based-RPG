from ItemsClass import Items


class Character:
    """Character master class"""
    def __init__(self, base_speed, base_attack, base_defense, base_hp ,race):
        """current is a variable that holds the current attribute e.g. current_speed = base_speed + item_given_speed"""
        self.current_speed = self.base_speed = base_speed
        self.current_attack = self.base_attack = base_attack
        self.current_defense = self.base_defense = base_defense
        # base_hp = characters hp , max_hp = base_hp + item_given_hp , current_hp is the current hp
        self.current_hp = self.max_hp = self.base_hp = base_hp
        self.race = race
        self.alive = True
        self.usable_items = []
        self.x = 0
        self.y = 0
        self.has_key = False
        # A list with the weapon and armor our character holds
        self.currently_equipped_weapons = []

    def _set_key(self, value):
        self.has_key = value

    def _get_key(self):
        return self.has_key

    def _set_x(self, value):
        self.x = value

    def _set_y(self,value):
        self.y = value

    def _get_y(self):
        return self.y

    def _get_x(self):
        return self.x

    def use_healing_item(self,items_name):
        for item in self.usable_items:
            if item.name == items_name:
                index = self.usable_items.index(item)
                self.change_stats = (self.usable_items.pop(self.usable_items.index(index)))
                break
            else:
                continue

    def change_stats(self,item):
        if item.name == "Potion" or item.name == "Medicinal Herb" or item.name == "Recovery":
            if self.max_hp == item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                return False
            else:
                self.current_hp = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
        elif item.name == "Old Axe" or item.name == "Hunter's Axe" or item.name == "Grand Axe":
            if item.name == "Grand Axe":
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    a_list = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                    self.current_attack = a_list[0]
                    self.current_speed = a_list[1]
                else:
                    return False
            else:
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    self.current_attack = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                else:
                    return False
        elif item.name == "Copper Sword" or item.name == "Iron Sword" or item.name == "Standard Bow" or item.name == "Long Bow":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_attack = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
            else:
                return False
        elif item.name == "Wooden Shield" or item.name == "Rusted Shield"  or item.name == "Scale Shield" or item.name == "Leather Shield":
            if item.name == "Leather Shield" or item.name == "Scale Shield":
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    a_list = item.item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                    self.current_defense = a_list[0]
                    self.current_speed = a_list[1]
                else:
                    return False
            else:
                if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                    self.current_defense = item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
                else:
                    return False
        return True

    def equip_item(self,item):
        if item.name == "Potion" or item.name == "Medicinal Herb" or item.name == "Recovery":
            self.usable_items.append(item)
        else:
            if self.change_stats(item):
                self.drop_item(item)
            else:
                return False

    def drop_item(self, item):
        if "Axe" in item.name or "Sword" in item.name or "Bow" in item.name:
            for curr_item in self.currently_equipped_weapons:
                if "Axe" in curr_item.name or "Sword" in curr_item.name or "Bow" in curr_item.name:
                    if self.change_stats(item):
                        self.currently_equipped_weapons.append(item)
                        return self.currently_equipped_weapons.pop(self.currently_equipped_weapons.index(curr_item))
                    else:
                        return False


class Human(Character):
    def __init__(self,base_speed=30,base_attack=20,base_defense=15,base_hp=25, race ="Human"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)
        cs = Items("Copper Sword")
        ws = Items("Wooden Shield")
        potion1 = Items("Potion")
        potion2 = Items("Potion")
        self.currently_equipped_weapons.append(cs)
        self.currently_equipped_weapons.append(ws)
        self.usable_items.append(potion1)
        self.usable_items.append(potion2)
        self.change_stats(cs)
        self.change_stats(ws)


class Elf(Character):
    def __init__(self, base_speed=35, base_attack=20, base_defense=10, base_hp=25, race="Elf"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)
        sb = Items("Standard Bow")
        ws = Items("Wooden Shield")
        potion = Items("Potion")
        m1 = Items("Medicinal Herb")
        m2 = Items("Medicinal Herb")
        self.currently_equipped_weapons.append(sb)
        self.currently_equipped_weapons.append(ws)
        self.usable_items.append(potion)
        self.usable_items.append(m1)
        self.usable_items.append(m2)
        self.change_stats(sb)
        self.change_stats(ws)








