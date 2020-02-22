# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"
    def print_room_description(self, player):
        print(str(self))
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def get_exits_string(self):
        return f"Exits: [{', '.join(self.get_exits())}]"
    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def get_coords(self):
        return [self.x, self.y]


['e', 'e', 'w', 'n', 'w', 'w', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 's', 's', 'w', 'n', 'w', 's', 'w', 'w', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 'n', 's', 'e', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'n', 'e', 'e', 'w', 'w', 's', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's', 's', 'e', 'e', 'w', 'n', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'w', 's', 'e', 'w', 'w', 'n', 's', 'w', 'w', 'n', 'e', 'w', 'n', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 'n', 'n', 's', 's', 's', 'e', 'e', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'e', 's', 'e', 's', 's', 's', 'e', 's', 's', 'w', 'w', 'n', 'n', 'n', 's', 's', 's', 'e', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'n', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'e', 's', 's', 's', 's', 's', 's', 'w', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'n', 's', 's', 's', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'e', 'e', 'e', 'e', 's', 's', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 's', 'n', 'w', 's', 'w', 'w', 'w', 's', 'w', 'w', 'e', 's', 'e', 's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 's', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 's', 'w', 's', 'n', 'e', 'n', 'e', 'n', 'e', 's', 's', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'w', 'e', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'n', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'e', 'n', 'n', 'n', 'e', 's', 'n', 'e', 'e', 's', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'e', 'n', 's', 's', 'w', 'e', 'n', 'e', 'n', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'n', 'n', 's', 'w', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'n', 'e', 'e', 's', 'w', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 's', 'n', 'w', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'e', 's', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'e', 'n', 'n', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 's', 'w', 'e', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 's', 'e', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 's', 'n', 'n', 'n', 'e', 'e', 's', 's', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'n', 'e', 's', 's', 'n', 'n', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'w', 'w', 's', 'e', 'e', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 's', 's', 'w', 's', 'n', 'e', 's', 's']