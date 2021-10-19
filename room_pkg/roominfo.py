import time
from room_pkg import mapinfo
from sql_pkg import sqlcmds
import helpers
from user_pkg import userinput
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
	userinput.check_input(x,y)

# METHOD TO HANDLE CINEMATICS
def play_cinematics(cinid):
	cinematics = sqlcmds.get_cinematics(cinid)
	if	cinematics is not None:
		for cin in cinematics:
			print('\n'+cin[0])
			time.sleep(1)
