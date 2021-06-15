from flask_mysqldb import MySQL
import mysql.connector



class Team:


    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='',database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()


        # Fetch all the row from a tkategori table using fetchall() method
    def fetch_all(self):
        self.conn.connect()
        # execute query in mysql database tteam
        self.cursor.execute('SELECT tteam.idteam, tteam.namateam, tteam.jeniskelamin, tteam.nomorhp, tteam.alamat, tteam.jabatan, tuser.userphoto, tuser.userid,tuser.userabout FROM `tteam` JOIN `tuser` WHERE tteam.userid = tuser.userid')
        # return result from fetchall method
        return self.cursor.fetchall()

        # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self, id):
        self.conn.connect()
        # execute query select one in mysql database tteam
        self.cursor.execute('SELECT tteam.idteam, tteam.namateam, tteam.jeniskelamin, tteam.nomorhp, tteam.alamat, tteam.jabatan, tuser.userphoto, tuser.userabout, tuser.userpassword FROM tteam JOIN tuser ON tteam.userid = tuser.userid WHERE tuser.userid = %s',(id,))
        # return result from fetchone method
        return self.cursor.fetchall()

        #insert data into tteam table
    def create(self, team=dict({})):
        # execute query insert in mysql database tteam
        self.cursor.execute('INSERT INTO tteam(namateam,jeniskelamin,nomorhp,alamat,jabatan,userid) VALUES (%s,%s,%s,%s,%s,%s)',
                            (team['namateam'], team['jeniskelamin'], team['nomorhp'], team['alamat'], team['jabatan'], team['userid']))
        self.cursor.execute(
            'INSERT INTO tuser(userid,userpassword,userphoto,hakakses,username) VALUES (%s,%s,%s,%s,%s)',
            (team['userid'], team['userpassword'], team['userphoto'], team['hakakses'], team['username']))
        # Commit your changes in the database
        self.conn.commit()

       # update data into tteam table
    def update(self, team=dict({})):
        # execute query update in mysql database tteam
        self.cursor.execute('UPDATE tteam SET namateam= %s, jeniskelamin= %s , nomorhp= %s, alamat=%s, jabatan=%s WHERE idteam= %s',
                            (team['namateam'], team['jeniskelamin'], team['nomorhp'], team['alamat'],team['jabatan'], team['idteam']))
        # Commit your changes in the database
        self.conn.commit()

    def updateprofileteam(self, team=dict({})):
        # execute query update in mysql database tteam
        self.cursor.execute('UPDATE tteam SET namateam= %s, jeniskelamin= %s , nomorhp= %s, alamat=%s WHERE userid= %s',
        (team['namateam'], team['jeniskelamin'], team['nomorhp'], team['alamat'], team['userid']))
        # Commit your changes in the database
        self.conn.commit()
        # delete data from tpegawai table where idpegawai are selected

    def delete(self, id):
        # execute query delete in mysql database tpegawai
        self.cursor.execute('DELETE FROM tteam WHERE idteam = %s', (id,))
        # Commit your changes in the database
        self.conn.commit()

    def setIncrement(self, maxid):
        # execute query auto increment in mysql database tteam
        self.cursor.execute('ALTER TABLE tteam AUTO_INCREMENT = %s ', (maxid+1,))
        # Commit your changes in the database
        self.conn.commit()

    def idteam(self):
        self.conn.connect()
        # execute query in mysql database tteam
        self.cursor.execute('SELECT MAX(idteam) FROM tteam')
        # return result from fetchone method
        return self.cursor.fetchone()[0]

    def count(self):
        self.conn.connect()
        # execute query delete in mysql database tteam
        self.cursor.execute('SELECT COUNT(idteam) FROM tteam WHERE 1')
        # Commit your changes in the database
        self.cursor.fetchone()[0]


