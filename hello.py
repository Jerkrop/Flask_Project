
from flask import Flask,render_template,request,redirect,url_for
#  this is all of the needed parts for the data base all that needs done is makeing it work
# And don't forget to download this so that it works
# pip install Flask psycopg2-binary
username = 'admin'
pswrd = 'welcome1'
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name)

@app.route('/error/<errType>')
def error(errType):
    return render_template('error.html', errType = errType)

@app.route("/login")
def hello_world():
    return render_template('login.html')

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        userpassed = request.form['pw']
        return redirect(url_for('welcome',name = user))
    else:
        return redirect(url_for('error',errType='Incorect Password'))

@app.route('/register')
def regi():
    return render_template('regestration.html')

@app.route('/register',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['Email']
        user = request.form['unr']
        password = request.form['pwr']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle')
        result = cur.fetchall()
        print(result)
        cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
        'VALUES(%s, %s, %s, %s, %s, %s, %s)',
        ('10001', name,  email , user , password , 'Bike1' , '$12,000'))
        conn.commit()
        cur.close()
        conn.close()
        return render_template('login.html')
    else:
        return render_template('login.html')
    
def registerz():

    if request.method == 'POST':
        user = request.form['unr']
        pass1 = request.form['pwr']
        if[user,pass1]:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('error',errType='Account already exists'))
    else:
        user = request.args.get('nm')
        userpassed = request.args.get('pw')
        if user == userpassed:
            return render_template('welcome.html')
        else:
            return redirect(url_for('error', errType ='Account already exists'))

import os
import psycopg2
def get_db_connection():
    conn = psycopg2.connect(
    "dbname=flask_db user=postgres host=localhost password=Meegee12"
)
    return conn

if __name__ == '__main__':
    app.run(debug=True)