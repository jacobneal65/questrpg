_connection = None

def get_connection():
    global _connection
    if not _connection:
        _connection = MySQLdb.connect(
				host="localhost",  user="olivander",
				password="olivander0",
				database="quest")
				
    return _connection

# List of stuff accessible to importers of this module. Just in case
__all__ = [ 'getConnection' ]

## Edit: actually you can still refer to db._connection
##         if you know that's the name of the variable.
## It's just left out from enumeration if you inspect the module
