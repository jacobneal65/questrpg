import sqlite3
import time
# ~ def check_database():
	# ~ #creates the quest database if it doesn't exist.
	# ~ conn = sqlite3.connect('quest.db')
	# ~ c = conn.cursor()
	# ~ c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rooms';")

	# ~ c.execute("SELECT * from rooms")
	# ~ returnvals = c.fetchone()

	# ~ if returnvals is None:
		# ~ print('empty')
	# ~ else:
		# ~ print(returnvals)
	# ~ conn.commit()
	# ~ conn.close()
	
def room_info(x, y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""
	SELECT name, description,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ? AND locationy = ?+1) AS n,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ? AND locationy = ?-1) AS s,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ?+1 AND locationy = ?) AS e,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ?-1 AND locationy = ?) AS w
	FROM rooms
	WHERE locationx = ? AND locationy = ?;
	"""
	inputparams = (x,y,x,y,x,y,x,y,x,y)
	
	c.execute(query,inputparams)
	returnvals = c.fetchone() 
	conn.close()
	return returnvals


def update_player(x, y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""
	UPDATE player
	SET
		locationx = ?,
		locationy = ?
	WHERE id = 1;
	"""
	c.execute(query,(x,y))
	conn.commit()
	conn.close()


def load_player():
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="SELECT * FROM player WHERE id = 1"
	
	c.execute(query)
	player = c.fetchone()
	conn.close()
	print('\n player loaded')
	time.sleep(0.8)
	return player

#----------------------TEST STILL----------------------
def get_trigger(x,y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""   
	SELECT keyword, newx, newy, cinematicid
    FROM room_triggers
    WHERE locationx = ? AND locationy = ?;
	"""
	inputparams = (x,y)
	
	c.execute(query,inputparams)
	returnvals = c.fetchone() 
	conn.commit()
	conn.close()
	return returnvals


#----------------------TEST STILL----------------------
def get_cinematics(myid):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""   
	SELECT description 
	FROM cinematics
	WHERE cinematicid = ?
	ORDER BY ordering;
	"""
	inputparams = (myid,)
	
	c.execute(query,inputparams)
	returnvals = c.fetchall() 
	conn.commit()
	conn.close()
	return returnvals


#----------------------TEST STILL----------------------
def get_map(x,y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	inputparams = (x,x,y,y)
	query ="""   
	SELECT locationx, locationy 
	FROM rooms
	WHERE locationx <= ?+2 AND locationx >= ?-2 AND locationy <= ?+2 AND locationy >= ?-2
	ORDER BY locationx ASC, locationy ASC;
	"""
	inputparams = (x,x,y,y)
	c.execute(query,inputparams)
	returnvals = c.fetchall() 
	conn.commit()
	conn.close()
	return returnvals






