from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
app=Flask(__name__,template_folder='template')

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'coba'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data")
    rv = cur.fetchall()
    cur.close()
    print(rv)
    return render_template('home.html',data=rv)    
   # return "<p></p>"

@app.route('/show/<string:id_data>')
def showId(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data WHERE id=%s",(id_data))
    rv = cur.fetchall()
    cur.close()
    print(rv)
    return rv

@app.route('/simpan',methods=["POST"])
def simpan():
    nama = request.form['nama']
    nim = request.form['NIM']
    cur = mysql.connection.cursor()    
    sql = "INSERT INTO data (nama, NIM) VALUES (%s, %s)"
    val = (nama,nim)
    cur.execute(sql, val)
    
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    nim = request.form['NIM']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE data SET nama=%s,NIM=%s WHERE id=%s", (nama,nim,id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='127.0.0.9',port=4455,debug=True) 