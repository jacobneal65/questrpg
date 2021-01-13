import time
import mysql.connector
import sqlconn

def invert_y(y):
	if y == 4:
		return 0
	elif y == 3:
		return 1
	elif y == 2:
		return 2
	elif y == 1:
		return 3
	elif y == 0:
		return 4
	else:
		return -1
		
		
def print_map(x,y):
	query = 'CALL Map(%s,%s);'
	query_tuple = (x, y)
	output = sqlconn.execute_query(query, query_tuple, 1) # one means grab multiples
	#print(output)
	
	#decided distance for a 5x5 matrix
	xstart = x-2 
	ystart = y-2
	
	yfixed = invert_y(y-ystart)
	xfixed = x-xstart
	#print(str(xfixed)+' '+str(yfixed))
	m = '-'
	
	T = [ [m, m, m, m, m], [m, m, m, m, m], [m, m, m, m, m], [m, m, m, m, m], [m, m, m, m, m] ]
	# NOTE: for some random reason, arrays go by the y value then the x. eg: T[2][1] means go down two rows, over one column. 
	for x in output:
		xmod = x[0] - xstart
		ymod = invert_y(x[1] - ystart)
		#print(str(xmod)+' and '+str(ymod))
		if xmod == xfixed and ymod == yfixed:
			T[ymod][xmod]='X'
		else:
			T[ymod][xmod]='#'

	#print array
	#print('  - - - - -')
	for r in T:
		print('|', end =' ') 
		for c in r:
			print(c,end = ' ')
		print('|')
	#print('  - - - - -')
