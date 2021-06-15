from flask_mysqldb import MySQL
import mysql.connector

class Message:
    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='', database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()

# Fetch all the row from a tkategori table using fetchall() method
    def fetch_all(self):
        self.conn.connect()
        # execute query in mysql database tpegawai
        self.cursor.execute('SELECT * from tmessage')
        # return result from fetchall method
        return self.cursor.fetchall()

     # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self, id):
        self.conn.connect()
        # execute query select one in mysql database tpegawai
        self.cursor.execute('SELECT * from tmessage WHERE idmessage = %s',(id,))
        # return result from fetchone method
        return self.cursor.fetchall()

      #insert data into tpegawai table
    def create(self, message=dict({})):
        # execute query insert in mysql database tpegawai
        self.cursor.execute('INSERT INTO tmessage(name,email,subject,message,tanggal_kirim,replied) VALUES (%s,%s,%s,%s,%s,%s)',
                            (message['name'], message['email'], message['subject'], message['message'],message['tanggal_kirim'], message['replied']))
        self.conn.commit()

    def update(self, message=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tmessage SET replied= %s,tanggal_dibalas= %s, replymessage=%s WHERE idmessage= %s',
                            (message['replied'], message['tanggal_dibalas'],message['replymessage'],message['idmessage']))
        # Commit your changes in the database
        self.conn.commit()

    def delete(self, id):
        # execute query delete in mysql database tMessage
        self.cursor.execute('DELETE FROM tmessage WHERE idmessage = %s', (id,))
        # Commit your changes in the database
        self.conn.commit()

    # Fetch all the row from a tkategori table using fetchall() method
    def fetch_no(self):
       self.conn.connect()
       # execute query in mysql database tmessage
       self.cursor.execute('SELECT * from tmessage WHERE replied="No"')
        # return result from fetchall method
       return self.cursor.fetchall()

    # Fetch all the row from a tkategori table using fetchall() method
    def fetch_new3message(self):
        self.conn.connect()
        # execute query in mysql database tmessage
        self.cursor.execute('SELECT * from tmessage WHERE replied="No" ORDER BY tanggal_kirim DESC Limit 3')
      # return result from fetchall method
        return self.cursor.fetchall()

