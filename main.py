import time
import sqlcmds
from roominfo import room_description
#--------BEGINNING--------
# Load the player and begin game loop
p = sqlcmds.load_player()
room_description(p[1], p[2])
