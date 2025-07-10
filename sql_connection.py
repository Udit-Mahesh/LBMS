<<<<<<< HEAD
import mysql.connector

__cnx=None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx=mysql.connector.connect(user='root',password='root',database='library')

=======
import mysql.connector

__cnx=None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx=mysql.connector.connect(user='root',password='root',database='library')

>>>>>>> 021fdf591c973b00f047735ae9a78bf0621bacba
    return __cnx