from flask_mysqldb import MySQL
import mysql.connector

class Subscribe:
    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='', database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()

# Fetch all the row from a tsubscribe table using fetchall() method
    def fetch_all(self):
        # execute query in mysql database tsubscribe
        self.cursor.execute('SELECT * from tsubscribe')
        # return result from fetchall method
        return self.cursor.fetchall()

     # Fetch a single row tsubscribe using fetchall() method.
    def fetch_one(self, id):
        # execute query select one in mysql database tsubscribe
        self.cursor.execute('SELECT * WHERE idsubscribe = %s',(id,))
        # return result from fetchone method
        return self.cursor.fetchall()

      #insert data into tsubscribe table
    def create(self, email):
        # execute query insert in mysql database tsubscribe
        self.cursor.execute('INSERT INTO `tsubscribe`(`email`) VALUES (%s)',(email,))
        self.conn.commit()

    def count(self):
        # execute query delete in mysql database tMessage
        self.cursor.execute('SELECT COUNT(idsubscribe) FROM tsubscribe WHERE 1')
        # Commit your changes in the database
        self.cursor.fetchone()


