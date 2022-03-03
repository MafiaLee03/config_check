from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Home'

@app.route('/login',methods=['GET'])
def login_from():
    return '''<form action='/login' method='post'>
              <p><input name='username'></p>
              <p><input name='password' type='password'></p>
              <p><button type='submit'>Sign In</button></p>
              </form>
    '''
@app.route('/login',methods=['POST'])
def login():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello admin</h3>'
    return '<h3>用户名或密码错误</h3>'

if __name__ == '__main__':
    app.run()