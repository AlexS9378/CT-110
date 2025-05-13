# Alex Sweat
# 5/12/2025
# P5HW
# A short text based adevnture game about finding an amulet and returning it into a temple to win the game.



import sys
import random

rooms = {
    'clearing': {
        'desc': "You're in a forest clearing. Paths lead north and east.",
        'exits': {'north': 'cave', 'east': 'river'},
        'items': []
    },
    'cave': {
        'desc': "A dark cave. You see a faint glow deeper inside. A path leads south.",
        'exits': {'south': 'clearing'},
        'items': ['amulet']
    },
    'river': {
        'desc': "A fast-flowing river blocks your path east. There’s a bridge, but it's broken. Paths lead west and north.",
        'exits': {'west': 'clearing', 'north': 'hut'},
        'items': []
    },
    'hut': {
        'desc': "An old hut. There's a rope here. Paths lead south.",
        'exits': {'south': 'river'},
        'items': ['rope']
    }
}

inventory = []
current_room = 'clearing'
turns_left = 10
has_won = False
# Print room
def print_room():
    room = rooms[current_room]
    print(f"\n{room['desc']}")
    if room['items']:
        print("You see:", ', '.join(room['items']))
    print("Exits:", ', '.join(room['exits'].keys()))
# Handle input
def handle_input(command):
    global current_room, has_won, turns_left

    parts = command.lower().split()
    if not parts:
        return

    action = parts[0]

    if action == 'go' and len(parts) > 1:
        direction = parts[1]
        if direction in rooms[current_room]['exits']:
            current_room = rooms[current_room]['exits'][direction]
        else:
            print("You can't go that way.")
    elif action == 'look':
        print_room()
    elif action == 'take' and len(parts) > 1:
        item = parts[1]
        if item in rooms[current_room]['items']:
            inventory.append(item)
            rooms[current_room]['items'].remove(item)
            print(f"You picked up the {item}.")
        else:
            print(f"No {item} here.")
    elif action == 'use' and len(parts) > 1:
        item = parts[1]
        if item not in inventory:
            print(f"You don't have a {item}.")
            return
        if item == 'rope' and current_room == 'river':
            print("You use the rope to cross the river safely.")
            rooms['river']['exits']['east'] = 'temple'
            rooms['temple'] = {
                'desc': "You reach a forgotten temple. A pedestal awaits the amulet.",
                'exits': {},
                'items': []
            }
        elif item == 'amulet' and current_room == 'temple':
            print("You place the amulet on the pedestal. Light surrounds you. You've won!")
            has_won = True
        else:
            print("You can't use that here.")
    else:
        print("Invalid command.")

# Main loop
print("Welcome to The Forgotten Forest!")
print("Find the Ancient Amulet and bring it to the temple before night falls (10 turns).")
print("Commands: go [direction], take [item], use [item], look")

while turns_left > 0 and not has_won:
    print_room()
    command = input("\n> ")
    handle_input(command)
    turns_left -= 1
    print(f"Turns left: {turns_left}")

if has_won:
    print("Congratulations! You survived the Forgotten Forest!")
else:
    print("Night falls and darkness consumes the forest... You are never seen again.")
