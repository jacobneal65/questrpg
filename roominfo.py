
#Gets the information for a room and then waits for user input.
def room_description(mycursor, x, y):
	
	query = 'CALL RoomInfo(%s,%s);'
	room_tuple = (x, y)
	mycursor.execute(query, room_tuple)
	currentroom = mycursor.fetchone()
	
	print('\n' + currentroom[2] + ' ')
	
	direct = '' #initialize
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
	
	#USER INPUT
	choice = input('Input: ')
	if choice == 'exit' or choice == 'quit':
		quit()
	if choice == 'n' or choice == 's' or choice == 'e' or choice == 'w':
		if choice == 'n':
			y+=1
		elif choice == 's':
			y-=1
		elif choice == 'e':
			x+=1
		elif choice == 'w':
			x-=1
		#run the script for checking room
		room_tuple = (x, y)
		mycursor.execute(query, room_tuple)
		currentroom = mycursor.fetchone()
		if currentroom is None:
			print('can\'t go that way')
		else:
			#if true run script to change player locationx and locationy
			query = 'CALL UpdatePlayer(%s,%s);'
			mycursor.execute(query, room_tuple)
			playera = mycursor.fetchone()
			#recursion of the room		
			room_description(mycursor, x, y) 	
			
			

		
		
	else:
		#run script for checking special commands
		print('not valid input. Maybe he will add more in the future')
		room_description(mycursor, x, y) 







