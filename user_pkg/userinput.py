from sql_pkg import sqlcmds
from room_pkg import roominfo

# METHOD TO HANDLE USER INPUT
def check_input(x,y):
	choice = input('Input: ')
	if choice == 'help' or choice == 'h':
		helpers.print_help()
		check_input(x,y)
	elif choice == 'exit' or choice == 'quit':
		quit()
	elif choice == 'room':
		roominfo.room_description(x,y)
	elif choice == 'restart':
			sqlcmds.update_player(1,1)
			roominfo.room_description(1,1)
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
		rm = sqlcmds.room_info(newx,newy)

		if rm is None:
			print('\ncan\'t go that way')
			check_input(x, y)
		else:
			#if true run script to change player locationx and locationy
			sqlcmds.update_player(newx,newy)
			roominfo.room_description(newx, newy)
	else:
		#look for unique commands
		triggers = sqlcmds.get_triggers(x,y)
		if triggers is not None:
			triggered = 0
			for trig in triggers:
				if choice == trig[0] and triggered == 0:
					#call cinematics
					roominfo.play_cinematics(trig[3])
					#run new room stuff
					newx=trig[1]
					newy=trig[2]
					#change player location to new room
					sqlcmds.update_player(newx,newy)
					roominfo.room_description(newx, newy)
					triggered = 1

			if triggered == 0:
				print('\n nothing happened')
				check_input(x, y)
		else:
			print('\n nothing happened')
			check_input(x, y)
