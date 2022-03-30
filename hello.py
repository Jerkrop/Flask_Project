from flask import Flask,render_template,request,redirect,url_for
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

if __name__ == '__main__':
    app.run(debug=True)