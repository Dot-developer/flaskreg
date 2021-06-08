from flask import Flask,request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
mysql= MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Austinlunatic@18'
app.config['MYSQL_DATABASE_DB'] = 'register'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

@app.route('/authentication',methods=['POST','GET'])
def authentication():
    if request.method == 'POST':
        uname = request.json["username"]
        pwd = request.json['password']

        conn = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT uname ,pswrd  FROM u_info WHERE username = %s",[uname])
        user = cursor.fetchone()

        if(user != None and len(user) > 0):
            uname = user[0]
            pswrd = user[1]
            if uname == uname:
                if pswrd == pwd:
                    return { "status": 200, "message":"Success" ,"username": uname }
                else:
                    return {"status": 404, "message":"Invalid Password", "username":""}
        else:
            return{"status": 404,"message": "Invalid Username", "username":""}
    else:
        return "Server is running"

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='127.0.0.1', port=8000, debug=True)

