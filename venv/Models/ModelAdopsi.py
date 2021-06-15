from flask_mysqldb import MySQL
import mysql.connector



class Adopsi:


    def __init__(self):
        # Open database connection
        self.conn = con = mysql.connector.connect(user='root', password='',database='catteams', host='localhost')
        # prepare a cursor object using cursor() method
        self.cursor = self.conn.cursor()


        # Fetch all the row from a tkucing table using fetchall() method
    def fetch_all(self):
        self.conn.connect()
        # execute query in mysql database tteam
        self.cursor.execute('SELECT tpengadopsi.idadopsi,tpengadopsi.noidentitaspengadopsi,tpengadopsi.namapengadopsi,tpengadopsi.emailpengadopsi,tpengadopsi.teleponpengadopsi,tpengadopsi.jeniskelamin,tpengadopsi.alamatpengadopsi,tpengadopsi.alasanadopsi,tpengadopsi.statusadopsi,tpengadopsi.idkucing,tkucing.namakucing,tkucing.jeniskucing,tkucing.photokucing  FROM `tpengadopsi` JOIN `tkucing` WHERE tpengadopsi.idkucing=tkucing.idkucing')
        # return result from fetchall method
        return self.cursor.fetchall()

        # Fetch a single row tpegawai using fetchall() method.
    def fetch_one(self, id):
        self.conn.connect()
        # execute query select one in mysql database tteam
        self.cursor.execute('SELECT * FROM tpengadopsi WHERE idadopsi = %s',(id,))
        # return result from fetchone method
        return self.cursor.fetchall()

    def fetch_one_bykucing(self, id):
         self.conn.connect()
         # execute query select one in mysql database tteam
         self.cursor.execute('SELECT * FROM tpengadopsi WHERE idkucing = %s', (id,))
         # return result from fetchone method
         return self.cursor.fetchall()

        #insert data into tpengadopsi table
    def create(self, adopsi=dict({})):
        # execute query insert in mysql database tpegawai
        self.cursor.execute('INSERT INTO tpengadopsi(idadopsi,noidentitaspengadopsi,namapengadopsi,emailpengadopsi,teleponpengadopsi,jeniskelamin,alamatpengadopsi,alasanadopsi,statusadopsi,idkucing) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            (adopsi['idadopsi'],adopsi['noidentitaspengadopsi'],adopsi['namapengadopsi'],adopsi['emailpengadopsi'],adopsi['teleponpengadopsi'],adopsi['jeniskelamin'],adopsi['alamatpengadopsi'],adopsi['alasanadopsi'],adopsi['statusadopsi'],adopsi['idkucing']))
        # Commit your changes in the database
        self.conn.commit()

        #update data into tpengadopsi tabel
    def update(self, adopsi=dict({})):
        # execute query insert in mysql database tpegawai
        self.cursor.execute('UPDATE tpengadopsi SET statusadopsi=%s WHERE idkucing=%s',(adopsi['statusadopsi'],adopsi['idkucing']))
        # Commit your changes in the database
        self.conn.commit()

    # Fetch all the row from a tkategori table using fetchall() method
    def fetch_newadoptionsubmition(self):
       self.conn.connect()
       # execute query in mysql database tmessage
       self.cursor.execute('SELECT * from tpengadopsi WHERE statusadopsi="Proses Pengajuan"')
        # return result from fetchall method
       return self.cursor.fetchall()






