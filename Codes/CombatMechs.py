from random import randint


class Combat:
    """
    @gk
    The class simulates a basic combat
    """

    def __init__(self, option):
        self.option = option

    def end_battle(self, char_hp, villains_hps_list):
        for i in villains_hps_list:
            if i <= 0:
                print("You defeated your foe")
                return False
            if char_hp <= 0:
                print("You were defeated")
                return False

    def combat(self, char_stats_list, villain_stats_list, villain_name, character_curr_item_list):
        plays_now = 0
        if char_stats_list[0] < villain_stats_list[0]:
            print("Villain goes first")
            plays_now = 1
        else:
            print("You go first")
            plays_now = 2

        round = 1
        while self.end_battle(char_stats_list[3], villain_stats_list[3]):
            option = 0
            item = -1
            curr_char_def = False
            curr_villain_def = False
            print("Round: " + str(round))
            if plays_now == 1:
                print("Foe's turn")
                villain_choice = randint(0, 1)
                if villain_choice == 0:
                    print(villain_name + " attacks")
                    if curr_char_def is True:
                        dmg = villain_stats_list[1] - char_stats_list[2] + 1
                        curr_char_def = False
                    else:
                        dmg = villain_stats_list[1] - char_stats_list[2]
                    char_stats_list[3] -= dmg
                    print("You received: " + dmg + " dmg")
                    print("Your current hp is " + char_stats_list[3])
                else:
                    print(villain_name + " defends")
                    curr_villain_def = True
                plays_now = 2
            if plays_now == 2:
                'make the characters combat menu'
                print("Your turn...")
                print("1. Attack")
                print("2. Defend")
                option = int(input("3. Use an item"))

                if option == 1:
                    print("You attack")
                    if curr_villain_def is True:
                        'dmg + 1 --> look at aggressiveness'
                        dmg = char_stats_list[1] + 1 - villain_stats_list[2] + 1
                        curr_villain_def = False
                    else:
                        dmg = char_stats_list[1] - villain_stats_list[2]
                    villain_stats_list[3] -= dmg
                    print("You dealt " + dmg + " dmg")
                    print("enemy's current hp is " + villain_stats_list[3])
                elif option == 2:
                    print("You are defending")
                    curr_char_def = True
                else:
                    print("Select one of the items in your possession")
                    for i in range(len(character_curr_item_list)):
                        print(i + character_curr_item_list[i])
                    item = int(input("Select one of the above"))
                    'waiting for characters function for applying items'