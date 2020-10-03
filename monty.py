from random import randint

import matplotlib.pyplot as plt
import random

nb_simulations = 100000

#----------------------------------------------------------------------------------------#
# simulation 1: player keeps his first choice 

win_s1_counts = 0

for i in range(nb_simulations):

	# select randomly behind which door is the car 

	winning_door = randint(1,3)

	# player pick a door 

	player_first_door = randint(1,3)

	# Game host open a door with a goat behind 

	l = [1,2,3]

	l.remove(winning_door)
	if player_first_door != winning_door : l.remove(player_first_door)

	game_host_opened = random.choice(l)

	# player keeps his first choice 

	if player_first_door == winning_door :

		win_s1_counts = win_s1_counts + 1

#----------------------------------------------------------------------------------------#
# simulation 2: player changes his first choice 

win_s2_counts = 0

for i in range(nb_simulations):

	# select randomly behind which door is the car 

	winning_door = randint(1,3)

	# player pick a door 

	player_first_door = randint(1,3)

	# Game host open a door with a goat behind 

	door_list = [1,2,3]

	door_list.remove(winning_door)
	if player_first_door != winning_door : door_list.remove(player_first_door)

	game_host_opened = random.choice(door_list)

	# player changes his first choice 

	door_list = [1,2,3]

	door_list.remove(game_host_opened)
	door_list.remove(player_first_door)

	player_new_door = door_list[0]

	if player_new_door == winning_door :

		win_s2_counts = win_s2_counts + 1


#----------------------------------------------------------------------------------------#
# print results

print( 1.0 * win_s1_counts / nb_simulations )
print( 1.0 * win_s2_counts / nb_simulations )




