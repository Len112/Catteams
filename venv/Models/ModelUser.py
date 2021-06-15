import mysql.connector

class User:
    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='',database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()


        # Fetch all the row from a tkategori table using fetchall() method
    def fetch_all(self):
        self.conn.connect()
        # execute query in mysql database tpegawai
        self.cursor.execute('SELECT * FROM tuser')
        # return result from fetchall method
        return self.cursor.fetchall()

        # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self, id):
        self.conn.connect()
        # execute query select one in mysql database tpegawai
        self.cursor.execute('SELECT * FROM tuser WHERE userid =%s',(id))
        # return result from fetchone method
        return self.cursor.fetchone()

    def update(self, user=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tuser SET userphoto= %s, username= %s, userabout=%s WHERE userid= %s',
                            (user['userphoto'], user['username'],user['userabout'],user['userid']))
        # Commit your changes in the database
        self.conn.commit()

    def updateuserteam(self, user=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tuser SET hakakses=%s,username= %s WHERE userid= %s',
                                (user['hakakses'], user['username'], user['userid']))
        # Commit your changes in the database
        self.conn.commit()

    def updateuserpassword(self, user=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tuser SET userpassword=%s WHERE userid= %s',
                                (user['userpassword'], user['userid']))
        # Commit your changes in the database
        self.conn.commit()
        # delete data from tpegawai table where idpegawai are selected

    def delete(self, id):
        # execute query delete in mysql database tpegawai
        self.cursor.execute('DELETE FROM tuser WHERE userid = %s', (id,))
        # Commit your changes in the database
        self.conn.commit()



