
def clear_screen():
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def add_space(direct):
	if len(direct) != 0:
		direct += ', '
	return direct


def get_directions(n,s,e,w):
	direct = ''
	if n != 0:
		direct += 'n'
	if s != 0:
		direct = add_space(direct)
		direct += 's'
	if e != 0:
		direct = add_space(direct)
		direct += 'e'
	if w != 0:
		direct = add_space(direct)
		direct += 'w'
	return direct


def print_help():
	print('\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
	print('In the world, you will interact with single word commands.\nThese can be an object in a room or a verb. \nHere are some general commands to get you started.')
	print('\nCommands: quit, restart, room.')
	print('Directions: n,s,e,w.')
	print('\n(Hint: a good start would be to go to the cockpit and type \'launch\')')
	print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
