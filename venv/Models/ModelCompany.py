from flask_mysqldb import MySQL
import mysql.connector



class Company:
    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='',database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()


        # Fetch all the row from a tkategori table using fetchall() method
    def fetch_all(self):
        # execute query in mysql database tteam
        self.cursor.execute('SELECT * FROM tcompany')
        # return result from fetchall method
        return self.cursor.fetchall()

        # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self):
        # execute query select one in mysql database tteam
        self.cursor.execute('SELECT * FROM `tcompany` WHERE 1')
        # return result from fetchone method
        return self.cursor.fetchall()

       # update data into tteam table
    def update(self, company=dict({})):
        # execute query update in mysql database tpegawai
        self.cursor.execute('UPDATE tcompany SET namecompany= %s, emailcompany= %s , nomorcompany= %s, alamatcompany=%s, photocompany=%s, aboutcompany=%s WHERE idcompany= %s',
                            (company['namecompany'], company['emailcompany'], company['nomorcompany'], company['alamatcompany'],company['photocompany'], company['aboutcompany'],company['idcompany']))
        # Commit your changes in the database
        self.conn.commit()



