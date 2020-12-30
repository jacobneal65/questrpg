import time
import mysql.connector
import mysqlconnection
from roominfo import room_description

# TODO
# add Jordan animations.
# setup a map system.

conn = mysqlconnection.get_connection() # This will always return the same object

#SETUP FIRST ROOM AND SQL CONNECTION
mydb = mysql.connector.connect(
  host="localhost",
  user="olivander",
  password="olivander0",
  database="quest"
)

mycursor = mydb.cursor()

class Player:
	def __init__(self, locationx=0, locationy=0):
		self.locationx = locationx
		self. locationy = locationy
		
	def load(self):
		#grabs the first player in db
		mycursor.execute("SELECT * FROM player WHERE id = 1")
		newplayer = mycursor.fetchone()
		self.locationx = newplayer[1]
		self.locationy = newplayer[2]




#Create our main player
player1 = Player()
player1.load()
room_description(mycursor, player1.locationx, player1.locationy)


