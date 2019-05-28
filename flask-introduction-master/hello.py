from flask import Flask, redirect, url_for,render_template,request
import time
app = Flask(__name__)

dict = {'AA001': 'AA001', 'AA002': 'AA002'}
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/login')
def login():
    return render_template('/index.html')

@app.route('/loginCred', methods = ['POST'])
def loginCred():
    user=request.form['userName']
    password=request.form['Password']
    
    if user in dict:
        if (dict.get(user)==password):
           
           return render_template('/nextpage.html', output ='Login SuccessFul')
         
        else:
             return render_template('/index.html', output ='Wrong Passoword')

    else:      
        return render_template('/index.html',output ='User Not Found. register User')

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run()



