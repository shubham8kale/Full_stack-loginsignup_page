from flask import Flask , render_template, request
import mysql.connector


app=Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')



@app.route('/signup',methods=['POST','GET'])
def signup_page():
    if request.method=='POST':
        user_first_name=request.form['first_name']
        user_last_name=request.form['last_name']
        user_email=request.form['user_email']
        user_password_1=request.form['user_password']
        user_password_2=request.form['user_password_2']
        user_gender=request.form['gender']
        user_age=request.form['user_age']

        if user_password_1==user_password_2:
            enter_value_to_db(user_first_name,user_last_name,user_email,user_password_1,user_gender,user_age)
        else:
            return render_template('signup.html')

        print("Sign up complete")
    return render_template('sign_up.html')

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$wapniL1842",
        db="sys"
        )
mycursor = mydb.cursor()

def enter_value_to_db(fname,lname,email,password,gender,age):


    mycursor.execute("INSERT INTO signup VALUES('{}','{}','{}','{}','{}','{}')".format(fname,lname,email,password,gender,age))
    mydb.commit()




@app.route('/login',methods=["POST","GET"])
def sample4():
    if request.method=="POST":
        email=request.form["user"]
        password=request.form["password"]

        sql = 'SELECT * FROM signup WHERE email = %s AND password = %s'
        val = (email , password)
        mycursor.execute(sql , val)
        account = mycursor.fetchone()
        if account:
            print("OK")
            return render_template('index.html')
        else:
            print("Not found")
            return render_template('sign_up.html')
    return render_template('login1.html')
