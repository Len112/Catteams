from flask_mysqldb import MySQL
import mysql.connector



class Kucing:


    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='',database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()


        # Fetch all the row from a tkucing table using fetchall() method
    def fetch_all(self):
        # execute query in mysql database tteam
        self.cursor.execute('SELECT * FROM tkucing')
        # return result from fetchall method
        return self.cursor.fetchall()

        # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self, id):
        # execute query select one in mysql database tteam
        self.cursor.execute('SELECT * FROM tkucing WHERE idkucing = %s',(id,))
        # return result from fetchone method
        return self.cursor.fetchall()

        #insert data into tkucing table
    def create(self, kucing=dict({})):
        # execute query insert in mysql database tpegawai
        self.cursor.execute('INSERT INTO tkucing(namakucing,jeniskucing,usiakucing,ukurankucing,jeniskelamin,photokucing,tentangkucing,statuskucing) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                            (kucing['namakucing'],kucing['jeniskucing'],kucing['usiakucing'],kucing['ukurankucing'], kucing['jeniskelamin'], kucing['photokucing'], kucing['tentangkucing'], kucing['statuskucing']))
        # Commit your changes in the database
        self.conn.commit()

       # update data into tkucing table
    def update(self, kucing=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tkucing SET namakucing= %s,jeniskucing= %s ,usiakucing=%s,ukurankucing=%s , jeniskelamin= %s , photokucing= %s, tentangkucing=%s, statuskucing=%s WHERE idkucing= %s',
                            (kucing['namakucing'],kucing['jeniskucing'],kucing['usiakucing'],kucing['ukurankucing'], kucing['jeniskelamin'], kucing['photokucing'],
                             kucing['tentangkucing'], kucing['statuskucing'], kucing['idkucing']))
        # Commit your changes in the database
        self.conn.commit()



    def delete(self, id):
        # execute query delete in mysql database tkucing
        self.cursor.execute('DELETE FROM tkucing WHERE idkucing = %s', (id,))
        # Commit your changes in the database
        self.conn.commit()




