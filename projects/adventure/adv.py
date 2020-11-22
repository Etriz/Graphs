from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque, defaultdict

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# ! do a bft so we try to get shortest path?

traversal_path = []
visited_rooms = set()

queue = deque()
queue.append(player.current_room.id)
# print(world.starting_room)

# while len(visited_rooms) < len(room_graph):
while len(queue) > 0:
    curr = queue.popleft()
    if curr not in visited_rooms:
        visited_rooms.add(curr)

        for neighbor in room_graph[curr][1].values():
            queue.append(neighbor)


print("visited_rooms")
print(visited_rooms)
"""
count = 0
while count in range(10):
    count += 1
    room_exits = player.current_room.get_exits()
    for e in room_exits:

        if player.current_room.get_room_in_direction(e) not in visited_rooms:
            print("-------------------")
            print(f"ATTEMPTING TO MOVE {e}")
            player.travel(e, True)
            visited_rooms.add(player.current_room)
            traversal_path.append(e)
            break
        elif player.current_room.get_room_in_direction(e) in visited_rooms:
            print("-------------------")
            print("BACKTRACKING")
            print(f"ATTEMPTING TO MOVE {e}")
            player.travel(e, True)
            break
"""
print("path")
print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
