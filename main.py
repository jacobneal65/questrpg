import time
from sql_pkg import sqlcmds
from room_pkg import roominfo
#--------BEGINNING--------
# Load the player and begin game loop
def main():
	p = sqlcmds.load_player() #load player p
	roominfo.room_description(p[1], p[2])


main()
