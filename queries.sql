https://dev.mysql.com/doc/mysql-getting-started/en/



CREATE DATABASE quest;


CREATE USER 'olivander'@'localhost' IDENTIFIED BY 'olivander0';
GRANT ALL PRIVILEGES ON *.* TO 'olivander'@'localhost' WITH GRANT OPTION;

Create room table

USE quest;
CREATE TABLE rooms
(
  id            INT unsigned NOT NULL AUTO_INCREMENT,    # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                    # Name of the room
  description    VARCHAR(1000) NOT NULL,                    # Description of the room
  locationx        INT NOT NULL,                            # x location of room
  locationy        INT NOT NULL,                            # y location of room
  PRIMARY KEY     (id)                                    # Make the id the primary key
);



#populate rooms
INSERT INTO rooms ( name, description, locationx, locationy) VALUES
('room1', 'You find yourself in the engine room of a ship you don\'t recognize. To the north is a hallway.', 1,1), #main ship area
('room2', 'the hallway leads cockpit. You should launch your ship.', 1,2), #cockpit
('room3', 'what a lovely skyline.', 10,1); #after launch

#Test Rooms
INSERT INTO rooms ( name, description, locationx, locationy) VALUES
('test1', 'room 2,2', 2,2),
('test2', 'room 0,2', 0,2),
('test3', 'room 1,0', 1,0),
('test4', 'room 1,-1', 1,-1);

#lets you see what is in rooms.

select * from rooms


#Create player

USE quest;
CREATE TABLE player
(
  id            INT unsigned NOT NULL AUTO_INCREMENT,    # Unique ID for the record
  locationx        INT NOT NULL,                            # x location of room
  locationy        INT NOT NULL,                            # y location of room
  PRIMARY KEY     (id)                                    # Make the id the primary key
);
INSERT INTO player (locationx, locationy) VALUES (1,1);

#Roominfo stored procedure                used to find all room information

DROP PROCEDURE IF EXISTS RoomInfo ;


CREATE PROCEDURE RoomInfo(IN xval INT, IN yval INT)

BEGIN
    SELECT id, name, description,
    EXISTS(SELECT 1 FROM rooms WHERE locationx = xval AND locationy = yval+1) AS n,
    EXISTS(SELECT 1 FROM rooms WHERE locationx = xval AND locationy = yval-1) AS s,
    EXISTS(SELECT 1 FROM rooms WHERE locationx = xval+1 AND locationy = yval) AS e,
    EXISTS(SELECT 1 FROM rooms WHERE locationx = xval-1 AND locationy = yval) AS w
    FROM rooms
    WHERE locationx = xval AND locationy = yval;
END


CALL RoomInfo(1,1)



#Update player location stored procedure    

select * from player where id = 1

CREATE PROCEDURE UpdatePlayer(IN xval INT, IN yval INT)

BEGIN
    UPDATE player
SET
        locationx = xval,
        locationy = yval
WHERE id = 1;
END

CALL UpdatePlayer(1,1)



CREATE TABLE room_triggers
(
  id            	INT unsigned NOT NULL AUTO_INCREMENT,   # Unique ID for the record
  keyword			VARCHAR(1000) NOT NULL,					# dont let them sql inject you dude 
  locationx			INT NOT NULL,                           # x location of room
  locationy        	INT NOT NULL,                           # y location of room
  newx       		INT NOT NULL,                           # new y location of room
  newy       		INT NOT NULL,                           # new y location of room
  cinematicid		int NOT NULL,                           # goes to cinematic table
  PRIMARY KEY     (id)                                    	# Make the id the primary key
);

CREATE TABLE cinematics
(
  id            	INT unsigned NOT NULL AUTO_INCREMENT,   # Unique ID for the record
  cinematicid		INT NOT NULL,                           # pull each page of desc for given trigger
  ordering			INT NOT NULL,                           # orderby to get descriptions running
  description       VARCHAR(1000) NOT NULL,					# the description
  PRIMARY KEY     (id)                                    	# Make the id the primary key
);

INSERT INTO room_triggers ( keyword, locationx, locationy, newx, newy, cinematicid) VALUES
('launch', 1,2,10,1,1)

CREATE PROCEDURE GetTrigger(IN xval INT, IN yval INT)
BEGIN
    SELECT keyword, newx, newy, cinematicid
    FROM room_triggers
    WHERE locationx = xval AND locationy = yval;
END

CALL GetTrigger(1,2)

INSERT INTO cinematics ( cinematicid, ordering, description) VALUES
(1,1, 'zoom'),
(1,2, 'such wow'),
(1,3, 'behold the stars');

CREATE PROCEDURE GetCinematics(IN myid INT)
BEGIN
  SELECT description 
  FROM cinematics
  WHERE cinematicid = myid
  ORDER BY ordering;
END


