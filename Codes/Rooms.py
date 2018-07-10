class Room:
    doors = {}
    enemies = {}
    barriers = {}

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.room_table = [[" " for i in range(width)] for j in range(height)]

    def __create_room(self):
        """
        Generate/Create the room.
        """
        self.place_doors()
        self.place_enemies()
        # self.place_barriersNearDoor(self.door3)
        self.print_room()

    def print_room(self):
        """
        Print the room as string for the user to see.
        """
        helper_line = []
        for i in range(width + 2):
            helper_line.append("-")

        print(" ".join(helper_line))
        for i in range(width):
            print("|", " ".join(self.room_table[i]), "|")

        print(" ".join(helper_line))

    def place_doors(self):
        """
        Automatically place the doors on the map.
        """
        for door in self.doors:
            self.room_table[door.position.x][door.position.y] = "="

    def place_enemies(self):
        """
        Automatically place the enemies on the map.
        """
        for enemy in self.enemies:
            self.room_table[enemy.position.x][enemy.position.y] = "O"  # TODO: place correct letters
