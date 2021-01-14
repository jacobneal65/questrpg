import time
import mapinfo
import sqlcmds

def clear_screen():
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#MAIN LOOP OF GAME. Gets room descriptions and user inputs etc
def room_description(x, y):

	currentroom = sqlcmds.room_info(x,y)
	clear_screen()
	mapinfo.print_map(x,y)
	print('\n' + currentroom[1] + ' ') # room description
	# initialize
	direct = ''
	if currentroom[2] != 0: # north
		direct += 'n'
	if currentroom[3] != 0:
		if len(direct) != 0:
			direct += ', ' # addspace
		direct += 's'
	if currentroom[4] != 0: # east
		if len(direct) != 0:
			direct += ', ' # addspace
		direct += 'e'
	if currentroom[5] != 0: # west
		if len(direct) != 0:
			direct += ', ' # addspace
		direct += 'w'
	if len(direct) != 0:
		print('directions: ' + direct)
	user_input(x,y)



# METHOD TO HANDLE USER INPUT
def user_input(x,y):
	choice = input('Input: ')
	if choice == 'help' or choice == 'h':
		print_help()
		user_input(x,y)	
	elif choice == 'exit' or choice == 'quit':
		quit()
	elif choice == 'room':
		room_description(x,y)
	elif choice == 'restart':
			sqlcmds.update_player(1,1)
			room_description(1,1)
	elif choice == 'n' or choice == 's' or choice == 'e' or choice == 'w':
		if choice == 'n':
			newy = y+1
			newx = x
		elif choice == 's':
			newy = y-1
			newx = x
		elif choice == 'e':
			newx = x+1
			newy = y
		elif choice == 'w':
			newx = x-1
			newy = y
		#run the script for checking room
		currentroom = sqlcmds.room_info(newx,newy)
		
		if currentroom is None:
			print('\ncan\'t go that way')
			user_input(x, y) 
		else:
			#if true run script to change player locationx and locationy
			sqlcmds.update_player(newx,newy)
			room_description(newx, newy) 		
	else: 
		#look for unique commands

		trigger = sqlcmds.get_trigger(x,y)
		if trigger is not None:
			if choice == trigger[0]:
				#call cinematics
				play_cinematics(trigger[3])
				#run new room stuff
				newx=trigger[1]
				newy=trigger[2]
				#change player location to new room
				sqlcmds.update_player(newx,newy)
				room_description(newx, newy) 	
			else:
				print('\n nothing happened')
				user_input(x, y) 
		else:
			print('\n nothing happened')
			user_input(x, y) 
		
		
# METHOD TO HANDLE CINEMATICS	
def play_cinematics(cinid):
	cin = sqlcmds.get_cinematics(cinid)
	if	cin is not None:
		for x in cin:
			print('\n'+x[0])
			time.sleep(1)


def print_help():
	print('\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	print('In the world, you will interact with single word commands.\nThese can be an object in a room or a verb. \nHere are some general commands to get you started.')
	print('\nCommands: quit, restart, room.')
	print('Directions: n,s,e,w.')
	print('\n(Hint: a good start would be to go to the cockpit and type \'launch\')')
	print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')





