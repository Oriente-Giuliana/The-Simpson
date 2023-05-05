from flask import render_template
from flask import Flask
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="THE_SIMPSON"
)

mycursor = mydb.cursor()

@app.route('/units')
def personaggiList():
    mycurson.execute("SELECT * FROM THE_SIMPSON")
    myresult=mycursor.fetchall()
    return render_template('the_simpson.html', units=myresult)