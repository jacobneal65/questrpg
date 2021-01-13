import time

import sqlconn
from roominfo import room_description

# TODO
# add Jordan animations.
# setup a map system.

class Player:
	def __init__(self, locationx=0, locationy=0):
		self.locationx = locationx
		self. locationy = locationy
		
	def load(self):
		#grabs the first player in db
		
		query = 'SELECT * FROM player WHERE id = 1'
		newplayer = sqlconn.execute_query(query)
		
		self.locationx = newplayer[1]
		self.locationy = newplayer[2]
		print('\n player loaded')
		time.sleep(0.8)
#Create our main player
player1 = Player()
player1.load()
room_description(player1.locationx, player1.locationy)


