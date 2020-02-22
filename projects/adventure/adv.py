from room import Room
from player import Player
from world import World
from util import Stack, Queue  # These may come in handy

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
#print(room_graph)
new_dict = {}
for i in room_graph: 
    new_dict[i] = room_graph[i][1]
print(new_dict)    
def get_adjacent(room_id):
    return new_dict[room_id]

world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['e', 'e', 'w', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'w', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 'n', 's', 'e', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'n', 'e', 'e', 'w', 'w', 's', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's', 's', 'e', 'e', 'w', 'n', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'w', 's', 'e', 'w', 'w', 'n', 's', 'w', 'w', 'n', 'e', 'w', 'n', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 'n', 'n', 's', 's', 's', 'e', 'e', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'e', 's', 'e', 's', 's', 'e', 's', 's', 'w', 'w', 'n', 'n', 'n', 's', 's', 's', 'e', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'n', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'e', 's', 's', 's', 's', 's', 's', 'w', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 's', 's', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'e', 'e', 'e', 'e', 's', 's', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 's', 'n', 'w', 's', 'w', 'w', 'w', 's', 'w', 'w', 'e', 's', 'e', 's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 's', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 's', 'w', 's', 'n', 'e', 'n', 'e', 'n', 'e', 's', 's', 'w', 's', 'w', 's', 's', 'w', 'e', 'n', 'w', 'e', 'n', 'e', 's', 's', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'w', 'e', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'n', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'e', 'n', 'n', 'n', 'e', 's', 'n', 'e', 'e', 's', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'e', 'n', 's', 's', 'w', 'e', 'n', 'e', 'n', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'n', 'n', 's', 'w', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'n', 'e', 'e', 's', 'w', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 's', 'n', 'w', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'e', 's', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'e', 'e', 'n', 'n', 'n', 'n', 'n', 'e', 's', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'n', 'e', 's', 's', 'n', 'n', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'w', 'w', 's', 'e', 'e', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 'n', 'n', 'w', 's', 'n', 'e', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 's', 'e', 's', 's', 'n', 'n', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's', 'e', 's', 'e', 'w', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'e', 's', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'n', 'w', 'w', 'n', 'w', 'w', 's', 's', 's', 's', 's', 'w', 's', 's', 'n', 'w', 's']


# my_visited = []
# while len(my_visited) < 4:
#     if player.current_room.id not in my_visited: 
#         exits = player.current_room.get_exits()
#         player.travel(exits[0])
#         next_room = player.current_room.id
#         print(next_room)
#         my_visited.append(player.current_room.id)

print('hello', player.current_room.id)
def get_all_paths():
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # # !!!! IMPLEMENT ME
        # return visited
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(player.current_room.id)
        # Create an empty set to store visited nodes
        visited = []
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                #print(v)
                #path = self.bfs(user_id, v)
                visited.append(v)
                # Then push all neighbors to the top of the stack
                for neighbor in list(get_adjacent(v).values()):
                    s.push(neighbor)
              
        return visited



#print(get_all_paths())
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
rooms_visited = []
for move in traversal_path:
    player.travel(move)
    rooms_visited.append(player.current_room.id)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#print(rooms_visited)    
sorted_list = sorted(rooms_visited)  
mylist = list(dict.fromkeys(sorted_list))
#print(mylist)
#print('this', list(get_adjacent(0).values()))
#print(get_all_paths(0))
# my_arr = ['e', 'e', 'w', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'e', 'e', 'w', 's', 'n', 'e', 'e', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n']

# print(len(my_arr))
my_array = ['']
big_array = my_array*30
print(big_array)

#breakpoint()
#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)

while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
        rooms_visited.append(player.current_room.id)
        print(player.current_room.id)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
    

