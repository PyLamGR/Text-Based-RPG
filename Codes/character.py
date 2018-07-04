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
        self.starter_pack = []
        self.usable_items = []
        #A list with the weapon and armor our character holds
        self.currently_equipped_weapons = []

    def change_stats(self,item):
        """Change characters stats by equipping items"""
        if item.name == "Potion" or item.name == "Recovery" or item.name == "Medicinal Herb":
            if self.current_hp == item.item_wilding_ability(self.race, self.current_hp, self.max_hp):
                return False #Current_hp == max_hp so healing is useless
            else:
                self.current_hp = item.stat_change(self.max_hp , self.current_speed ,self.current_attack
                , self.current_defense, self.current_speed)
        elif item.name == "Old Axe" or item.name == "Hunter's Axe" or item.name == "Grand Axe":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_attack = self.base_attack + item.stat_change(self.max_hp, self.current_speed, self.current_attack, self.current_defense, self.current_speed )
            else:
                return False  # Character can not use this item
        elif item.name == "Copper Sword" or item.name == "Iron Sword" or item.name == "Standard Bow"  or item.name == "Long Bow":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_attack = self.base_attack + item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)
            else:
                return False # Character can not use this item
        elif item.name == "Wooden Shield" or item.name == "Rusted Shield" or item.name == "Leather Shield" or item.name == "Scale Shield":
            if item.item_wielding_ability(self.race, self.current_hp, self.max_hp):
                self.current_defense = self.base_defense + item.stat_change(self.max_hp, self.current_hp, self.current_attack, self.current_defense, self.current_speed)

    def equip_items(self,item):
        if item.name == "Position" or "Recovery" or "Medicinal Herb":
            self.usable_items.append(item)
        else:
            self.change_stats(item)

    def use_healing_item(self, item):
        self.change_stats(item)
        self.usable_items.remove(item)

    def apply_starter_pack(self):
        for item in self.starter_pack:
            if item.name != "Position" and item.name != "Medicinal Herb":
                self.change_stats(item)
                self.currently_equipped_weapons.append(item)


    def equip_weapons(self,item):
        if "Sword" in item.name or "Axe" in item.name or "Bow" in item.name:
            type_of_item = "Attack"
        else:
            type_of_item = "Defense"
        self.drop_item(item,type_of_item)

    def drop_item(self,new_item,type_of_item):
        if type_of_item == "Attack":
            for item in self.currently_equipped_weapons:
                if "Sword" in item.name or "Axe" in item.name or "Bow" in item.name:
                    self.currently_equipped_weapons.append(new_item)
                    return self.currently_equipped_weapons.pop(self.currently_equipped_weapons.index(item))

        else:
            for item in self.currently_equipped_weapons:
                if "Shield" in item.name:
                    self.currently_equipped_weapons.append(new_item)
                    return self.currently_equipped_weapons.pop(self.currently_equipped_weapons.index(item))



class Human(Character):
    def __init__(self,base_speed=30,base_attack=20,base_defense=15,base_hp=25, race ="Human"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)
        cs = Items("Copper Sword")
        ws = Items("Wooden Shield")
        potion1 = Items("Potion")
        potion2 = Items("Potion")
        self.starter_pack.append(cs)
        self.starter_pack.append(ws)
        self.starter_pack.append(potion1)
        self.starter_pack.append(potion2)
        self.apply_starter_pack()

class Elf(Character):
    def __init__(self, base_speed=35, base_attack=20, base_defense=10, base_hp=25, race="Elf"):
        super().__init__(base_speed, base_attack, base_defense, base_hp, race)
        sb = Items("Standard Bow")
        ws = Items("Wooden Shield")
        potion = Items("Potion")
        m1 = Items("Medicinal Herb")
        m2 = Items("Medicinal Herb")
        self.starter_pack.append(sb)
        self.starter_pack.append(ws)
        self.starter_pack.append(potion)
        self.starter_pack.append(m1)
        self.starter_pack.append(m2)
        self.apply_starter_pack()










