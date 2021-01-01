import sqlconn
import time

#MAIN LOOP OF GAME. Gets room descriptions and user inputs etc
def room_description(x, y):
	
	query = 'CALL RoomInfo(%s,%s);'
	room_tuple = (x, y)
	currentroom = sqlconn.execute_query(query,room_tuple)
	
	print('\n' + currentroom[2] + ' ')
	#initialize
	direct = ''
	if currentroom[3] != 0: #north
		direct += 'n'
	if currentroom[4] != 0:
		if len(direct) != 0:
			direct += ' ' #addspace
		direct += 's'
	if currentroom[5] != 0: #east
		if len(direct) != 0:
			direct += ' ' #addspace
		direct += 'e'
	if currentroom[6] != 0: #west
		if len(direct) != 0:
			direct += ' ' #addspace
		direct += 'w'
	if len(direct) != 0:
		print('directions: ' + direct)
	user_input(x,y)



# METHOD TO HANDLE USER INPUT
def user_input(x,y):
	choice = input('Input: ')
	if choice == 'exit' or choice == 'quit':
		quit()
	elif choice == 'restart':
			sqlconn.update_query( 'CALL UpdatePlayer(%s,%s);',(1,1))	#restart game
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
		#run the script for checking room
		query = 'CALL RoomInfo(%s,%s);'
		newcoor = (newx, newy)
		currentroom = sqlconn.execute_query(query,newcoor)
		
		if currentroom is None:
			print('can\'t go that way')
			user_input(x, y) 
		else:
			#if true run script to change player locationx and locationy
			query = 'CALL UpdatePlayer(%s,%s);'
			sqlconn.update_query(query,newcoor)	
			room_description(newx, newy) 		
	else: 
		#look for unique commands
		query = 'CALL GetTrigger(%s,%s);'
		location = (x, y)
		trigger = sqlconn.execute_query(query,location)
		if trigger is not None:
			if choice == trigger[0]:
				#call cinematics
				play_cinematics(trigger[3])
				#run new room stuff
				newx=trigger[1]
				newy=trigger[2]
				newcoor = (newx, newy)
				#change player location to new room
				query = 'CALL UpdatePlayer(%s,%s);'
				playera = sqlconn.update_query(query,newcoor)
				room_description(newx, newy) 	
			else:
				print('\n nothing happened')
				user_input(x, y) 
		else:
			print('\n nothing happened')
			user_input(x, y) 
		
		
# METHOD TO HANDLE CINEMATICS	
def play_cinematics(cinid):
	query = 'CALL GetCinematics(%s);'
	cintuple = (cinid,)
	cin = sqlconn.execute_query(query, cintuple,1)	
	if	cin is not None:
		for x in cin:
			print('\n'+x[0])
			time.sleep(1)
