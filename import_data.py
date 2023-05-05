# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS THE_SIMPSON")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS THE_SIMPSON.personaggi(
    Name VARCHAR(30),
    Surname VARCHAR(30),
    gender VARCHAR(30),
    PRIMARY KEY (Unit)
  );""")

#Delete data from the table personaggi
mycursor.execute("DELETE FROM THE_SIMPSON.personaggi")
mydb.commit()

#Read data from a csv file
Simpsons_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
Simpsons_data = Simpsons_data.fillna('Null')
print(Simpsons_data.head(20))

#Fill the table 
for i,row in Simpsons_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO THE_SIMPSON.personaggi VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM THE_SIMPSON.personaggi")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)