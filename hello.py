from flask import Flask,render_template,request,redirect,url_for
#  this is all of the needed parts for the data base all that needs done is makeing it work
# And don't forget to download this so that it works
# pip install Flask psycopg2-binary
import os
# import psycopg2

# conn = psycopg2.connect(
#     host = 'localhost',
#     database = 'flask_db',
#     # dont forget to use your password for pgadmin
#     password = 'Meegee12',
#     user = 'postgres'
# )
# cur = conn.cursor()

# # This below will make the table

# cur.execute("CREATE TABLE bicycle (id serial PRIMARY KEY, name text NOT NULL, email varchar (150) NOT NULL,username varchar (150) NOT NULL,password varchar (150) NOT NULL,bicycleName text NOT NULL,bicyclePrice int NOT NULL);")
# # cur.execute('CREATE TABLE bicycle (id varchar (10) NOT NULL',
# #                                  'name text NOT NULL',
# #                                  'email varchar (150) NOT NULL',
# #                                  'username varchar (150) NOT NULL',
# #                                  'password varchar (150) NOT NULL',
# #                                  'bicycleName text NOT NULL',
# #                                  'bicyclePrice int (10) NOT NULL)')

# # # all the values still need to be added but i put in an example for you 
# def function_(var1,var2, var3, var4, var5, var6, var7):
#     cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
#     'VALUES(%s, %s, %s, %s, %s, %s, %s)',
#     (var1, var2, var3, var4, var5, var6, var7))



# function_('10001', 'Jeremy', 'Testemail@gmail.com', 'Jerkrop' , 'Yes' , 'Brookes' , '50')
# function_('10002', 'Ezra', 'Ezra@gmail.com', 'EzraB' , 'Yes' , 'BlackBicycle' , '150')
# function_('10003', 'Zach', 'Zach@gmail.com', 'ZachD' , 'Yes' , 'OrangeBicycle' , '170')
# function_('10004', 'Ashton', 'Ashton@gmail.com', 'Ashtonw' , 'Yes' , 'BlueBicycle' , '100')
# function_('10005', 'Justice', 'Finn@gmail.com', 'Justicev' , 'Yes' , 'GreenBicycle' , '170')
# function_('10006', 'Gabriel', 'Gabe@gmail.com', 'GabeD' , 'Yes' , 'RedBroonieBicycle' , '200')
# function_('10007', 'Finn', 'Finn@gmail.com', 'FinnM' , 'Yes' , 'QuintonBicycle' , '250')
# function_('10008', 'Carlos', 'CarlosA@gmail.com', 'CarlosA' , 'Yes' , 'HarleyDavidsonBicycles' , '260')
# function_('10009', 'William', 'Will@gmail.com', 'WillB' , 'Yes' , 'FordBicycles' , '270')
# function_('10010', 'Dinnese', 'Dinnese@gmail.com', 'DinneseH' , 'Yes' , 'TopSubaruBicycles' , '280')

username = 'admin'
pswrd = 'welcome1'
app = Flask(__name__)
userpass = [['admin','password']]

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
        if [user,userpassed] in userpass:
            return redirect(url_for('welcome',name = user))
        else:
            return redirect(url_for('error',errType='Incorect Password'))

@app.route('/register')
def regi():
    return render_template('regestration.html')

@app.route('/register',methods=['POST', 'GET'])
def registerz():
    if request.method == 'POST':
        user = request.form['unr']
        pass1 = request.form['pwr']
        if[user,pass1] not in userpass:
            userpass.append([user,pass1])
            return redirect(url_for('login'))
        else:
            return redirect(url_for('error',errType='Account already exists'))
    else:
        user = request.args.get('nm')
        userpassed = request.args.get('pw')
        if [user,userpassed] in userpass:
            return redirect(url_for('welcome',name = user))
        else:
            return redirect(url_for('error', errType ='Account already exists'))
# conn.commit()
# cur.close()
# conn.close()
if __name__ == '__main__':
    app.run(debug=True)