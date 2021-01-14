
import sqlite3

def drop_tables():
	conn = sqlite3.connect('quest.db')
	c = conn.cursor()
	c.execute("drop table cinematics;")
	c.execute("drop table rooms;")
	c.execute("drop table player;")
	c.execute("drop table room_triggers;")
	conn.commit()
	conn.close()

drop_tables()


#creates the quest database if it doesn't exist.
conn = sqlite3.connect('quest.db')

c = conn.cursor()
c.execute(""" 
CREATE TABLE rooms
(
	name      	CHAR(150) 	NOT NULL,            
	description   	CHAR(1000) 		NOT NULL,                 
	locationx     	INT 			NOT NULL,                          
	locationy     	INT 			NOT NULL        
);
""")

c.execute(""" 
INSERT INTO rooms ( name, description, locationx, locationy) VALUES
('room1', 'You find yourself in the engine room of a ship you do not recognize. 
To the north is a hallway.', 1,1),
('room2', 'the hallway leads cockpit. You should launch your ship.', 1,2), 
('room3', 'what a lovely skyline.', 10,1);
""")

c.execute(""" 
INSERT INTO rooms ( name, description, locationx, locationy) VALUES
('test1', 'room 2,2', 2,2),
('test2', 'room 0,2', 0,2),
('test3', 'room 1,0', 1,0),
('test4', 'room 1,-1', 1,-1),
('test5', 'room 1,3', 1,3),
('test6', 'room 1,4', 1,4),
('test7', 'room 1,5', 1,5),
('test8', 'room 3,2', 3,2),
('test9', 'room 4,2', 4,2),
('test10', 'room 5,2', 5,2),
('test11', 'room 6,2', 6,2);

""")

c.execute(""" 
CREATE TABLE player
(
  id			   INT NOT NULL,
  locationx        INT NOT NULL,
  locationy        INT NOT NULL
);
""")

c.execute(""" 
	INSERT INTO player (id, locationx, locationy) VALUES (1,1,1);
""")

c.execute(""" 
CREATE TABLE room_triggers
(
  keyword			VARCHAR(1000) NOT NULL,
  locationx			INT NOT NULL,        
  locationy        	INT NOT NULL,          
  newx       		INT NOT NULL,     
  newy       		INT NOT NULL,         
  cinematicid		int NOT NULL                   
);
""")

c.execute(""" 
CREATE TABLE cinematics
(
  cinematicid		INT NOT NULL,               
  ordering			INT NOT NULL,             
  description       VARCHAR(1000) NOT NULL
);
""")

c.execute(""" 
INSERT INTO room_triggers ( keyword, locationx, locationy, newx, newy, cinematicid) VALUES
('launch', 1,2,10,1,1)
""")

c.execute(""" 
INSERT INTO cinematics ( cinematicid, ordering, description) VALUES
(1,1, 'zoom'),
(1,2, 'such wow'),
(1,3, 'behold the stars');
""")


conn.commit()
conn.close()


