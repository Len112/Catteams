from flask import Flask, render_template, url_for, redirect, request, flash, session, make_response#import modul-modul yang disediakan flask
from Models import ModelTeam, ModelUser, ModelMessage, ModelSubscribe, ModelCompany, ModelKucing, ModelAdopsi
from datetime import datetime
import mysql.connector
import os, time
from werkzeug.utils import secure_filename
from werkzeug.security import  generate_password_hash, check_password_hash
from werkzeug.serving import run_simple
from flask_mail import Mail, Message
import pdfkit
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

app = Flask(__name__, static_url_path='/static')
app.config["UPLOAD_FOLDER"]="./static/assets/images/faces" #path untuk upload folder
app.config["UPLOAD_FOLDER2"]="./static/assets/img/portfolio" #path untuk upload folder
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 #size file upload
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg'] #extension file
Team = ModelTeam.Team() #membuat objek baru dari ModelTeam
User = ModelUser.User()#membuat objek baru dari ModelUser
SendMessage = ModelMessage.Message()#membuat objek baru dari ModelMessage
Subscribe = ModelSubscribe.Subscribe()#membuat objek baru dari ModelSubscribe
Company = ModelCompany.Company()#membuat objek baru dari ModelCompany
Kucing = ModelKucing.Kucing()#membuat objek baru dari ModelKucing
Adopsi = ModelAdopsi.Adopsi()#membuat objek baru dariModelAdopsi

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USE_SSL']= False
app.config['MAIL_USERNAME']= 'pratamaell112@gmail.com'
app.config['MAIL_PASSWORD']= 'Ellen_112'


mail = Mail(app)

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route("/")
def home():
    onecompany = Company.fetch_all() # membuat variabel untuk menyimpan row data dari database
    listteam = Team.fetch_all()  # membuat variabel untuk menyimpan row data dari database
    listkucing = Kucing.fetch_all()  # membuat variabel untuk menyimpan row data dari database
    return render_template("home.html", DataC=dict({'onecompany':onecompany}),data = dict({'listteam':listteam}), dataK=dict({'listkucing':listkucing}))

@app.route("/404")
def page404():
    return render_template("404.html")

@app.route("/505")
def page505():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        return render_template("505.html")

#Membuat route menuju menu dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get("userid"):#Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else :
        oneteam = Team.fetch_one(session["userid"])
        UnrepliedMessage= SendMessage.fetch_no()
        countunrepliedmessage = len(UnrepliedMessage)
        Subscribers =Subscribe.fetch_all()
        countsubscribe = len(Subscribers)
        newmessage = SendMessage.fetch_new3message()
        return render_template("dashboard.html",DataU=dict({'oneteam': oneteam}),
                               DataCM=countunrepliedmessage, DataCS=countsubscribe, DataNew=dict({'newmessage':newmessage}))

#Membuat route menuju Sign In page
@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == "POST":  # jika method post
        # maka data request form di masukan kedalam suatu variabel
        userid = request.form['userid'],
        userpassword = request.form['userpassword']
        # mengambil data user berdasarkan user id yang di dapat dari request form
        user = User.fetch_one(userid)
        if user is None:  # jika row data dari database yang telah diambil adalah None
            flash("User id dan user password salah")  # maka akan memberikan message
            return redirect("signin")  # menuju sign in
        else:  # jika tidak (row data ada)
            # cek password apakah sudah sesuai atau belum menggunakan function check_password_hash
            if check_password_hash(user[1], userpassword):
                # jika sesuai maka dibuat session dan memasukan data-data user yang login kedalam session
                session['userid'] = user[0]
                session['userphoto'] = user[2]
                session['hakakses'] = user[3]
                session['username'] = user[4]
                # kemudian menuju dashboard
                return redirect('dashboard')
            else:  # jika tidak maka
                # maka akan memberikan message bahwa password tidak sesuai
                flash("user password tidak sesuai")
                return redirect("signin")  # kembali menuju signin
    else:
        # merender template sign in (view)
        return render_template("signin.html")

#Membuat route untuk auntentifikasi
@app.route('/authentication', methods=['GET','POST'])
def authentication():
    if request.method == "POST":  # jika method post
        # maka data request form di masukan kedalam suatu variabel
        userid = request.form['userid'],
        userpassword = request.form['userpassword']
        # mengambil data user berdasarkan user id yang di dapat dari request form
        user = User.fetch_one(userid)
        if user is None:  # jika row data dari database yang telah diambil adalah None
            flash("User id dan user password salah")  # maka akan memberikan message
            return redirect("signin")  # menuju sign in
        else:  # jika tidak (row data ada)
            # cek password apakah sudah sesuai atau belum menggunakan function check_password_hash
            if check_password_hash(user[1], userpassword):
                # jika sesuai maka dibuat session dan memasukan data-data user yang login kedalam session
                session['userid'] = user[0]
                session['userphoto'] = user[2]
                session['hakakses'] = user[3]
                session['username'] = user[4]
                # kemudian menuju dashboard
                return redirect('dashboard')
            else:  # jika tidak maka
                # maka akan memberikan message bahwa password tidak sesuai
                flash("user password tidak sesuai")
                return redirect("signin")  # kembali menuju signin
    else:
        return redirect("signin")

@app.route('/signout')
def signout():
    session.clear()#menghapus session
    return redirect('signin') # menuju ke halaman signin


#Membuat route menuju menu pegawai
@app.route('/team')
def team():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        if session["hakakses"] == "Contributor": #jika hak akses kasir maka
            return redirect('505')  # akan menuju halaman error
        else:
            oneteam = Team.fetch_one(session["userid"])
            listteam = Team.fetch_all()  # membuat variabel untuk menyimpan row data dari database
            idteam = Team.idteam() # membuat variabel untuk menyimpan row data dari database
            newmessage = SendMessage.fetch_new3message()
            #merender template pegawai (view) dan memasukan data yang dari variabel listpegawai
            return render_template("team.html",  data = dict({'listteam':listteam}),
                                   dataID = idteam, DataU=dict({'oneteam': oneteam}), DataNew=dict({'newmessage':newmessage}))

#Membuat route menuju insert pegawai dengan metode post
@app.route('/insertteam', methods=['GET','POST'])
def insertteam():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        # membuat variabel  new_ pegawai untuk menampung data dari form input pegawai baru
        if request.method == 'POST':
            photo = request.files['userphoto']
            filename = secure_filename(photo.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    return flash("File tidak sesuai"), 400
                photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo.filename))
                photoname = photo.filename
            else:
                photoname = "pic-1.png"
            password = generate_password_hash(request.form['userpassword'])
            new_team = {
                'namateam': request.form['namateam'],
                'jeniskelamin': request.form['jeniskelamin'],
                'nomorhp': request.form['nomorhp'],
                'alamat': request.form['alamat'],
                'jabatan': request.form['jabatan'],
                'userid': request.form['userid'],
                'hakakses': request.form['jabatan'],
                'username': request.form['namateam'],
                'userphoto': photoname,
                'userpassword': password
            }
            Team.create(team=new_team)
            flash("Data berhasil ditambahkan")
        # redirect ke link team
        return redirect(url_for('team'))


#Membuat route menuju update team dengan metode post
@app.route('/updateteam', methods=['POST'])
def updateteam():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        # membuat variabel  updated_team untuk menampung data hasil form edit data team
        if request.method == 'POST':
            updated_team = {
                'idteam': request.form['idteam'],
                'namateam': request.form['namateam'],
                'jeniskelamin': request.form['jeniskelamin'],
                'nomorhp': request.form['nomorhp'],
                'alamat': request.form['alamat'],
                'jabatan': request.form['jabatan'],
                'hakakses': request.form['jabatan'],
                'username': request.form['namateam'],
                'userid': request.form['userid']
            }
            # mengoper data dari variabel ke update function di model team agar dapat mengeksekusi perintah query update data
            Team.update(team=updated_team)
            User.updateuserteam(user=updated_team)
            flash("Data berhasil diubah")
            # redirect ke link pegawai
        return redirect(url_for('team'))

#Membuat route untuk menghapus data pegawai dengan idpegawai tertentu dengan metode GET
@app.route('/deleteteam/<idteam>/<userid>', methods=['GET'])
def deleteteam(idteam,userid):
    if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
        return redirect('404')  # akan menuju halaman error
    else:
        # mengoper data id team ke delete function di model pegawai agar dapat mengeksekusi perintah query delete data
        Team.delete(idteam)
        User.delete(userid) #megoper data ke model agar dapat memnjalankan perintah query
        idteam = Team.idteam()  # membuat variabel untuk menyimpan row data dari database
        Team.setIncrement(idteam) #megoper data ke model agar dapat memnjalankan perintah query
        flash("Data berhasil dihapus")
        # redirect ke link pegawai
        return redirect(url_for('team'))

@app.route('/myprofile')
def myprofile():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        #membuat variabel penampung data dari database model pegawai
        onecompany = Company.fetch_all()
        oneteam = Team.fetch_one(session["userid"])
        newmessage = SendMessage.fetch_new3message()
        return render_template('myprofile.html', DataU=dict({'oneteam':oneteam}),
                               DataC=dict({'onecompany':onecompany}), DataNew=dict({'newmessage':newmessage})) # menampilkan myprofile html

    # Membuat route menuju update myprofile dengan metode post
@app.route('/updatedmyprofile', methods=['POST'])
def updatedmyprofile():
    if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
        return redirect('404')  # akan menuju halaman error
    else:
        if request.method == "POST":
            photo = request.files['userphoto']
            filename = secure_filename(photo.filename) #mendapatkan nama dari file yang diupload
            if filename != '':#jika filename  tidak kosong
                file_ext = os.path.splitext(filename)[1]#maka mengambil extension file
                if file_ext not in app.config['UPLOAD_EXTENSIONS']: #jika file extension sesuai dengan yang sudah dideklarasikan
                    return flash("File tidak sesuai"), 400 #maka akan memberika pesan tidak sesuai
                # jika file extension sesuai maka akan disimpan di path yang telah ditentukan
                photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo.filename))
                photoname = photo.filename
            else:
                photoname = request.form['userphoto2']#jika filename kosong maka variabel phononame akan tetap sama dengan yang dulu
            # membuat variabel  updated_myprofile untuk menampung data hasil form edit data pegawai
            updated_myprofile = {
                'userid': request.form['userid'],
                'namateam': request.form['namateam'],
                'jeniskelamin': request.form['jeniskelamin'],
                'nomorhp': request.form['nomorhp'],
                'alamat': request.form['alamat'],
                'userphoto': photoname,
                'username': request.form['namateam'],
                'userabout': request.form['userabout']
            }
            # mengoper data dari variabel ke update function di model team agar dapat mengeksekusi perintah query update data
            Team.updateprofileteam(team=updated_myprofile)
            # mengoper data dari variabel ke update function di model user agar dapat mengeksekusi perintah query update data
            User.update(user=updated_myprofile)
            flash("Data berhasil diubah")#memberikan pesan
        # redirect ke link pegawai
        return redirect(url_for('myprofile'))

@app.route('/editpassword')
def editpassword():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        #membuat variabel penampung data data dari model team
        oneteam = Team.fetch_one(session["userid"])
        newmessage = SendMessage.fetch_new3message()
        # menampilkan template editpassword dan memassing data dari model team ke dalam template
        return render_template('editpassword.html', DataU=dict({'oneteam':oneteam}),DataNew=dict({'newmessage':newmessage})) # menampilkan myprofile html

@app.route('/updatepassword', methods=['POST','GET'])
def updatepassword():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        if request.method =="POST":
            password = generate_password_hash(request.form['userpassword'])  # mengkode password
            # membuat variabel penampung data yang dibutuhkan untuk update password
            updated_password = {
                'userpassword': password,
                'userid': session['userid']
            }
            User.updateuserpassword(user=updated_password)  # memanggil dan mengeksekusi perintah dari model user
            # memberikan flask message
            session.clear()
            flash("Password berhasil diubah, silahkan login kembali")
            return redirect('signin')  # menuju ke editpassword

@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    replied = 'No'
    if request.method == 'POST':
        message = {
            'email': request.form['email'],
            'name': request.form['name'],
            'subject': request.form['subject'],
            'message': request.form['message'],
            'tanggal_kirim': datetime.now(),
            'replied': replied
        }
        SendMessage.create(message=message)
        flash("Pesan anda berhasil terkirim")
        return redirect('/#contact')



#Membuat route menuju menu message
@app.route('/message')
def message():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        if session["hakakses"] == "Contributor": #jika hak akses kasir maka
            return redirect('505')  # akan menuju halaman error
        else:
            oneteam = Team.fetch_one(session["userid"])
            listmessage = SendMessage.fetch_all()
            newmessage = SendMessage.fetch_new3message()
            #merender template pegawai (view) dan memasukan data yang dari variabel listpegawai
            return render_template("message.html",  data = dict({'listmessage':listmessage}),
                                   DataU=dict({'oneteam': oneteam}), DataNew=dict({'newmessage':newmessage}))

@app.route('/replymessage', methods=['POST','GET'])
def replymessage():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        if request.method == 'POST':
            email = request.form['email']
            name = request.form['nama']
            subject = request.form['subject']
            pembuka = request.form['pembuka']
            replymessage = request.form['replymessage']
            balasan = pembuka + replymessage
            msg = Message(subject, sender=app.config.get("MAIL_USERNAME"), recipients=[email])
            msg.body = balasan
            mail.send(msg)
            replied = 'Yes'
            updated_message = {
                'replied': replied,
                'tanggal_dibalas': datetime.now(),
                'replymessage': replymessage,
                'idmessage': request.form['idmessage']
            }
            SendMessage.update(message=updated_message)
            flash("pesan berhasil terbalas")
            return redirect('message')

@app.route('/subscribe', methods=['POST','GET'])
def subscribe():
    if request.method == 'POST':
        email= request.form['email']
        Subscribe.create(email)
        flash("Terimakasih telah Subscribe ! tunggu kabar terbaru kami !")
        return redirect('/#Subscribe')
    else:
        if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
            return redirect('404')  # akan menuju halaman error
        else:
            if session["hakakses"] == "Contributor": #jika hak akses kasir maka
                return redirect('505')  # akan menuju halaman error:
            else :
                oneteam = Team.fetch_one(session["userid"])
                listsubscribe = Subscribe.fetch_all()
                newmessage = SendMessage.fetch_new3message()
                return render_template('subscribe.html', data=dict({'listsubscribe': listsubscribe}),
                                       DataU=dict({'oneteam': oneteam}), DataNew=dict({'newmessage':newmessage}))

@app.route('/sendnewsletter', methods=['POST','GET'])
def sendnewsletter():
    if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
        return redirect('404')  # akan menuju halaman error
    else:
        if request.method == 'POST':
            subject = request.form['subject']
            message = request.form['message']
            listsubscribe = Subscribe.fetch_all()
            for email in listsubscribe:
                msg = Message(subject, sender=app.config.get("MAIL_USERNAME"), recipients=[email[1]])
                msg.body = message
                time.sleep(2)
                mail.send(msg)
            flash("Newsletter berhasil terkirim")
            return redirect('subscribe')

@app.route('/mycompany')
def mycompany():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        if session["hakakses"] == "Contributor": #jika hak akses Contributor maka
            return redirect('505')  # akan menuju halaman error
        else:
            # membuat variabel penampung data dari database model pegawai
            oneteam = Team.fetch_one(session["userid"])
            onecompany = Company.fetch_all()
            newmessage = SendMessage.fetch_new3message()
            return render_template('mycompany.html', DataC=dict({'onecompany': onecompany}),
                                   DataU=dict({'oneteam': oneteam}),
                                   DataNew=dict({'newmessage': newmessage}))  # menampilkan mycompany html


#Membuat route menuju update team dengan metode post
@app.route('/updatecompany', methods=['POST'])
def updatecompany():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        photo = request.files['photocompany']
        filename = secure_filename(photo.filename)  # mendapatkan nama dari file yang diupload
        if filename != '':  # jika filename  tidak kosong
            file_ext = os.path.splitext(filename)[1]  # maka mengambil extension file
            if file_ext not in app.config[
                'UPLOAD_EXTENSIONS']:  # jika file extension sesuai dengan yang sudah dideklarasikan
                return flash("File tidak sesuai"), 400  # maka akan memberika pesan tidak sesuai
            # jika file extension sesuai maka akan disimpan di path yang telah ditentukan
            photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo.filename))
            photoname = photo.filename
        else:
            photoname = request.form[
                'photocompany2']  # jika filename kosong maka variabel phononame akan tetap sama dengan yang dulu
        # membuat variabel  updated_team untuk menampung data hasil form edit data team
        if request.method == 'POST':
            updated_company = {
                'idcompany': request.form['idcompany'],
                'namecompany': request.form['namecompany'],
                'emailcompany': request.form['emailcompany'],
                'nomorcompany': request.form['nomorcompany'],
                'alamatcompany': request.form['alamatcompany'],
                'photocompany': photoname,
                'aboutcompany': request.form['aboutcompany']
            }
            # mengoper data dari variabel ke update function di model team agar dapat mengeksekusi perintah query update data
            Company.update(company=updated_company)
            flash("Data berhasil diubah")
            # redirect ke link pegawai
        return redirect(url_for('mycompany'))

#Membuat route menuju menu daftar kucing
@app.route('/kucing')
def kucing():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        oneteam = Team.fetch_one(session["userid"])
        listkucing = Kucing.fetch_all()  # membuat variabel untuk menyimpan row data dari database
        idteam = Team.idteam()  # membuat variabel untuk menyimpan row data dari database
        newmessage = SendMessage.fetch_new3message()
        # merender template pegawai (view) dan memasukan data yang dari variabel listpegawai
        return render_template("kucing.html", data=dict({'listkucing': listkucing}),
                               dataID=idteam, DataU=dict({'oneteam': oneteam}),
                               DataNew=dict({'newmessage': newmessage}))

#Membuat route menuju insert kucing dengan metode post
@app.route('/insertkucing', methods=['GET','POST'])
def insertkucing():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        # membuat variabel  new_ pegawai untuk menampung data dari form input pegawai baru
        if request.method == 'POST':
            photo = request.files['photokucing']
            filename = secure_filename(photo.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    return flash("File tidak sesuai"), 400
                photo.save(os.path.join(app.config["UPLOAD_FOLDER2"], photo.filename))
                photoname = photo.filename
            else:
                photoname = "kucing_profile.jpg"
            new_kucing = {
                'namakucing': request.form['namakucing'],
                'jeniskucing': request.form['jeniskucing'],
                'usiakucing': request.form['usiakucing'],
                'ukurankucing': request.form['ukurankucing'],
                'jeniskelamin': request.form['jeniskelamin'],
                'photokucing': photoname,
                'tentangkucing': request.form['tentangkucing'],
                'statuskucing': "Siap di Adopsi",
            }
            Kucing.create(kucing=new_kucing)
            flash("Data berhasil ditambahkan")
        # redirect ke link team
        return redirect(url_for('kucing'))

#Membuat route menuju update kucing dengan metode post
@app.route('/updatekucing', methods=['POST'])
def updatekucing():
    if not session.get("userid"): #Jika session tidak mendapat userid (tidak sign in)
        return redirect('404') #akan menuju halaman error
    else:
        # membuat variabel  new_ pegawai untuk menampung data dari form input pegawai baru
        if request.method == 'POST':
            photo = request.files['photokucing']
            filename = secure_filename(photo.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    return "none"
                photo.save(os.path.join(app.config["UPLOAD_FOLDER2"], photo.filename))
                photoname = photo.filename
            else:
                photoname = request.form['photokucing']
            new_kucing = {
                'namakucing': request.form['namakucing'],
                'jeniskucing': request.form['jeniskucing'],
                'usiakucing': request.form['usiakucing'],
                'ukurankucing': request.form['ukurankucing'],
                'jeniskelamin': request.form['jeniskelamin'],
                'photokucing': photoname,
                'tentangkucing': request.form['tentangkucing'],
                'statuskucing': "Siap di Adopsi",
                'idkucing': request.form['idkucing'],
            }
            Kucing.update(kucing=new_kucing)
            flash("Data berhasil diedit")
        # redirect ke link team
        return redirect(url_for('kucing'))

#Membuat route untuk menghapus data pegawai dengan idpegawai tertentu dengan metode GET
@app.route('/deletekucing/<idkucing>', methods=['GET'])
def deletekucing(idkucing):
    if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
        return redirect('404')  # akan menuju halaman error
    else:
        # mengoper data id team ke delete function di model pegawai agar dapat mengeksekusi perintah query delete data
        Kucing.delete(idkucing)
        flash("Data berhasil dihapus")
        # redirect ke link pegawai
        return redirect(url_for('kucing'))

# Membuat route untuk menghapus data pegawai dengan idpegawai tertentu dengan metode GET
@app.route('/catportfoliodetail/<idkucing>', methods=['GET'])
def catportfoliodetail(idkucing):
    onecompany = Company.fetch_all()  # membuat variabel untuk menyimpan row data dari database
    onekucing = Kucing.fetch_one(idkucing) # membuat variabel untuk menyimpan row data dari database

    return render_template('catportfoliodetail.html', DataC=dict({'onecompany': onecompany}), DataOK=dict({'onekucing': onekucing}))

# Membuat route untuk menghapus data pegawai dengan idpegawai tertentu dengan metode GET
@app.route('/ajukanadopsi/<idkucing>', methods=['GET','POST'])
def ajukanadopsi(idkucing):
    if request.method == 'GET':
        onecompany = Company.fetch_all()  # membuat variabel untuk menyimpan row data dari database
        onekucing = Kucing.fetch_one(idkucing)  # membuat variabel untuk menyimpan row data dari database

        return render_template('adoptionsubmitionform.html', DataC=dict({'onecompany': onecompany}),
                               DataOK=dict({'onekucing': onekucing}))
    if request.method == 'POST':
        listkucing = Kucing.fetch_all()  # membuat variabel untuk menyimpan row data dari database
        new_adopsi = {
            'idadopsi' : request.form['idadopsi'],
            'noidentitaspengadopsi': request.form['noidentitaspengadopsi'],
            'namapengadopsi': request.form['namapengadopsi'],
            'emailpengadopsi': request.form['emailpengadopsi'],
            'teleponpengadopsi': request.form['teleponpengadopsi'],
            'jeniskelamin': request.form['jeniskelamin'],
            'alamatpengadopsi': request.form['alamatpengadopsi'],
            'alasanadopsi': request.form['alasanadopsi'],
            'statusadopsi': "Proses Pengajuan",
            'idkucing': request.form['idkucing'],
        }
        Adopsi.create(adopsi=new_adopsi)
        flash("Berhasil mengajukan adopsi")
        return redirect(url_for('catportfoliodetail', idkucing=idkucing))

@app.route("/adopsi", methods=['GET','POST','POST1'])
def adopsi():
    if not session.get("userid"):  # Jika session tidak mendapat userid (tidak sign in)
        return redirect('404')  # akan menuju halaman error
    else:
        if request.method == 'GET':
            oneteam = Team.fetch_one(session["userid"])
            listadopsi = Adopsi.fetch_all()  # membuat variabel untuk menyimpan row data dari database
            idteam = Team.idteam()  # membuat variabel untuk menyimpan row data dari database
            newmessage = SendMessage.fetch_new3message()
            # merender template pegawai (view) dan memasukan data yang dari variabel listpegawai
            return render_template("adoption.html", data=dict({'listadopsi': listadopsi}),
                                   dataID=idteam, DataU=dict({'oneteam': oneteam}),
                                   DataNew=dict({'newmessage': newmessage}))
        if request.method == 'POST':
            if request.form['statusadopsi'] !="":
                new_adopsi = {
                    'idkucing': request.form['idkucing'],
                    'statusadopsi': request.form['statusadopsi']
                }
                Adopsi.update(adopsi=new_adopsi)
                if request.form['statusadopsi'] =="Adopsi ditolak":
                    Kucing.updatestatus(kucing=({'idkucing': request.form['idkucing'],
                    'statuskucing': "Siap di Adopsi"}))
                return redirect(url_for('adopsi'))
            if request.form['verifikasidata'] =="lengkap":
                new_adopsi = {
                    'idkucing': request.form['idkucing'],
                    'statusadopsi': "Adopsi Berhasil"
                }
                Adopsi.update(adopsi=new_adopsi)
                Kucing.updatestatus(kucing=({'idkucing': request.form['idkucing'],
                                                 'statuskucing': "Telah di Adopsi"}))
                return redirect(url_for('adopsi'))
            if request.form['verifikasidata'] =="tidaklengkap":
                new_adopsi = {
                    'idkucing': request.form['idkucing'],
                    'statusadopsi': "Adopsi Gagal"
                }
                Kucing.updatestatus(kucing=({'idkucing': request.form['idkucing'],
                                             'statuskucing': "Siap di Adopsi"}))
                Adopsi.update(adopsi=new_adopsi)
                return redirect(url_for('adopsi'))

@app.route('/<name>/<location>')
def pdf(name,location):
    options = {
        "enable-local-file-access":None
    }
    photo ="static/assets/img/portfolio/kucing.jpg"
    rendered = render_template('pdftemplatepengajuanadopsi.html',name=name,location=location)
    pdf=pdfkit.from_string(rendered,False,configuration=config,options=options)

    response=make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response



# main untuk menjalankan app
if __name__ == '__main__' :
    app.secret_key="EllenPratama"
    app.run(debug=True)