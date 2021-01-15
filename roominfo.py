import time
import mapinfo
import sqlcmds
import helpers

#MAIN LOOP OF GAME. Gets room descriptions and user inputs etc.
def room_description(x, y):
	rm = sqlcmds.room_info(x,y)
	helpers.clear_screen()
	#ART
	if rm[6] is not None:
		art = sqlcmds.get_art(rm[6])
		print('   ======'+art[0] +'======'+'\n' +art[1])
	#MAP
	mapinfo.print_map(x,y)
	#DESCRIPTION
	print('\n' + rm[1] + ' ')
	
	directions = helpers.get_directions(rm[2], rm[3], rm[4], rm[5])
	if len(directions) != 0:
		print('directions: ' + directions)
	user_input(x,y)



# METHOD TO HANDLE USER INPUT
def user_input(x,y):
	choice = input('Input: ')
	if choice == 'help' or choice == 'h':
		helper.print_help()
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
		rm = sqlcmds.room_info(newx,newy)
		
		if rm is None:
			print('\ncan\'t go that way')
			user_input(x, y) 
		else:
			#if true run script to change player locationx and locationy
			sqlcmds.update_player(newx,newy)
			room_description(newx, newy) 		
	else: 
		#look for unique commands
		triggers = sqlcmds.get_triggers(x,y)
		if triggers is not None:
			triggered = 0
			for trig in triggers:
				if choice == trig[0] and triggered == 0:
					#call cinematics
					play_cinematics(trig[3])
					#run new room stuff
					newx=trig[1]
					newy=trig[2]
					#change player location to new room
					sqlcmds.update_player(newx,newy)
					room_description(newx, newy)
					triggered = 1
					 	
			if triggered == 0:
				print('\n nothing happened')
				user_input(x, y) 
		else:
			print('\n nothing happened')
			user_input(x, y) 
		
		
# METHOD TO HANDLE CINEMATICS	
def play_cinematics(cinid):
	cinematics = sqlcmds.get_cinematics(cinid)
	if	cinematics is not None:
		for cin in cinematics:
			print('\n'+cin[0])
			time.sleep(1)







