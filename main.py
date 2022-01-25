# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Validation
import Encryption
import CurTime
from ExHand import MyException
from flask import Flask, request, render_template

import database

count = 0
app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # global count
    # count += 1
    # fname = request.get_data()
    d = request.form
    fname = d.get('firstname')
    lname = d.get('lastname')
    number = d.get('number')
    email = d.get('email')
    passwd = d.get('passwd')
    reason = ""
    try:
        if not (Validation.isNameValid(fname) and Validation.isNameValid(lname)):
            raise (MyException("Name or Surname is Invalid"))
        print("Name and Surname is valid")
        if not Validation.isPasswdValid(passwd):
            raise (MyException("Password is Invalid"))
        print("Password is valid")
        if not Validation.isNumberValid(number):
            raise (MyException("Mobile Number is not Valid"))
        print("Mobile number is valid")
        if not Validation.isEmailValid(email):
            raise (MyException("Email is Invalid"))
        print("Email is Valid")
        if Validation.userExists(email):
            raise (MyException("User already exists"))
        print("User does not exists")
        timest = CurTime.getCurrTime()
        passwd = Encryption.encrypt(passwd) + Encryption.encrypt(timest)
        database.insertIntoUser(fname, lname, number, email, passwd, timest)
        reason = "Account Created Successfully"
    except MyException as e:
        reason = str(e)
    except Exception as e:
        reason = ''

    # print('fname',d.get('firstname'))
    # print('lname', d.get('lastname'))
    # print('number', d.get('number'))
    # print('email', d.get('email'))
    # print('passwd', d.get('passwd'))
    # fname = request.values['firstname']
    # email = request.form['email']
    # passwd = request.form['passwd']
    # print(type(passwd))
    return render_template('signup.html', info=f"{reason}")


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    d = request.form
    email = d.get('email')
    passwd = d.get('passwd')
    info = ""
    try:
        if not (Validation.isEmailValid(email) and Validation.userExists(email)):
            raise (MyException("User does not exist"))
        prevtime = database.getTimest(email)
        curpasswd = Encryption.encrypt(passwd) + Encryption.encrypt(prevtime)

        if not (database.getPasswd(email) == curpasswd):
            raise (MyException("Password is not correct"))

        timest = CurTime.getCurrTime()
        passwd = Encryption.encrypt(passwd) + Encryption.encrypt(timest)
        database.updateTime(email,timest)
        database.updatePasswd(email,passwd)
        info="SuccessFully Logined"
        return render_template("content.html")
    except MyException as e:
        info = str(e)
    except Exception as e:
        print(e)
        info = ""

    # TODO Do it by today only
    return render_template('signin.html', info=f"{info}")

# @app.route("/content")
# def content():
#     render_template("/content.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
