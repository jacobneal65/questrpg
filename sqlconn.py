import mysql.connector

#USED TO PULL INFORMATION
def execute_query(query, tuples=None, multiple = 0): #multiple parameter is used if you need to pull multiple lines from db
	conn = mysql.connector.connect(
				host="localhost",  
				user="olivander",
				password="olivander0",
				database="quest")	
	mycursor = conn.cursor()
	if tuples != None:
		#print('tuples: '+ str(tuples))
		mycursor.execute(query, tuples)
		if multiple==1:
			returnvals = mycursor.fetchall()
		else:
			returnvals = mycursor.fetchone()
		mycursor.close()
		
	else:
		mycursor.execute(query)
		if multiple==1:
			returnvals = mycursor.fetchall()
		else:
			returnvals = mycursor.fetchone()
	
	conn.close()
	return returnvals
	
#USED TO UPDATE INFORMATION
def update_query(query, tuples):
	conn = mysql.connector.connect(
				host="localhost",  
				user="olivander",
				password="olivander0",
				database="quest")
				
	mycursor = conn.cursor()
	mycursor.execute(query, tuples)
	conn.commit() #commit the changes
	mycursor.close()
	conn.close()
	#print('updated')
	


#https://stackoverflow.com/questions/5504340/python-mysqldb-connection-close-vs-cursor-close
#mydb = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database, charset="utf8")
#cursor = mydb.cursor()
#query = "INSERT INTO tablename (text_for_field1, text_for_field2, text_for_field3, text_for_field4) VALUES (%s, %s, %s, %s)"
#cursor.execute(query, (field1, field2, field3, field4))
#mydb.commit()
#cursor.close()
#mydb.close()
