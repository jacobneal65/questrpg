import sqlite3
import time
	
def room_info(x, y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""
	SELECT name, description,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ? AND locationy = ?+1) AS n,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ? AND locationy = ?-1) AS s,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ?+1 AND locationy = ?) AS e,
	EXISTS(SELECT 1 FROM rooms WHERE locationx = ?-1 AND locationy = ?) AS w,
	artid
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

#--------work on this more later
def get_triggers(x,y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""   
	SELECT keyword, newx, newy, cinematicid
    FROM room_triggers
    WHERE locationx = ? AND locationy = ?;
	"""
	inputparams = (x,y)
	
	c.execute(query,inputparams)
	returnvals = c.fetchall() 
	conn.close()
	return returnvals


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
	conn.close()
	return returnvals


def get_map(x,y):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""   
	SELECT locationx, locationy 
	FROM rooms
	WHERE locationx <= ?+2 AND locationx >= ?-2 AND locationy <= ?+2 AND locationy >= ?-2
	ORDER BY locationx ASC, locationy ASC;
	"""
	inputparams = (x,x,y,y)
	c.execute(query,inputparams)
	returnvals = c.fetchall() 
	conn.close()
	return returnvals

def get_art(artid):
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	query ="""   
	SELECT name, image 
	FROM art
	WHERE artid = ?
	"""
	inputparams = (artid,)
	c.execute(query,inputparams)
	returnvals = c.fetchone()
	conn.close()
	return returnvals




