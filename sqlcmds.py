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
	c.execute(query,(x,y,x,y,x,y,x,y,x,y))
	returnvals = c.fetchone()
	conn.close()
	print(returnvals)
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
	conn.commit
	conn.close()


def load_player():
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="SELECT * FROM player WHERE id = 1"
	
	c.execute(query)
	player = c.fetchone() # or c.fetchall()
	conn.close()
	print('\n player loaded')
	time.sleep(0.8)
	return player


def template_method():
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	inputparams = (1,1)
	query ="""     """
	c.execute(query,inputparams)
	returnvals = c.fetchone() # or c.fetchall()
	conn.commit()
	conn.close()
	return returnvals
