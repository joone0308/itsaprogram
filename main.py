# import statements
import time

# west
# room1
# 	three potions, one is poison
# room2
# 	tiny hole
# room3
# 	dark room, but a light in the distance
# east

# global variables
game_map = {
	"room1": { "east": "room2" },
	"room2": { "east": "room3", "west": "room1" },
	"room3": { "west": "room2" }
}

# functions

# main game loop
def main():
	print('You find yourself in a room.')
	print('')
	print('Pick a potion.')
	print('Potion puzzle placeholder.')

main()