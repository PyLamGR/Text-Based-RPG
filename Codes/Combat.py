import random as r
from CharacterClass import Character
from enemy import Enemy

"""@Iznogohul"""

def end_of_battle():
    Enemy.die
    if Character.current_hp <= 0:
        print("You Dead")
        Character.alive = False
        return False
    elif not(Enemy.alive):
        print("You Won")
        return False
    else:
        True

 
def combat():
    dmg=0
    if Character.current_speed < Enemy.speed:
        plays = True
    elif Character.current_speed > Enemy.speed:
        plays = False
    else:
        print("Equal Speeds")
    while end_of_battle:
        if plays:
            print("Your turn")
            print("1.Attack")
            print("2.Defend")
            print("3.Use an item")
            choice = int(input)
            if choice == 1:
                option = Enemy.choose_action
                if option is False:
                    dmg -= 1
                dmg += max(Character.current_attack - Enemy.defence, 0)
                print("You dealt "+dmg+"damage")
                print(Enemy.name+"current hp is"+Enemy.health)
            elif choice == 2:
                print("You are defending")
                Character.curr_char_def = True
            else:
                for i in range(len(Character.ItemsList)):
                    print((i+1)+"." + Character.ItemsList[i])
                item_choice = int(input("Choose item to use:"))
                Character.change_stats(item_choice)

        else:
            print(Enemy.name + "'s turn")
            choice = r.randint(0, 1)
            if choice == 0:
                if Character.curr_char_def is True:
                    dmg -= 1
                    Character.curr_char_def = False
                dmg += max((Enemy.current_attack -
                            Character.current_defense), 0)
                Character.current_hp -= dmg
                print("You received:"+dmg+"damage")
                print("Current Hp:" + Character.current_hp)
