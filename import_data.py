import mysql.connector
import pandas as pd

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

# Create the database (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS THE_SIMPSON")

# Switch to the database
mycursor.execute("USE THE_SIMPSON")
mycursor.execute("DROP TABLE  IF EXISTS THE_SIMPSON.personaggi")
# Create the table for the first CSV data (personaggi) if it doesn't exist
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS personaggi(
    nome VARCHAR(30),
    cognome VARCHAR(30),
    genere VARCHAR(30),
    PRIMARY KEY (nome)
  );""")

# Delete data from the table personaggi
mycursor.execute("DELETE FROM personaggi")
mydb.commit()

# Read data from the first CSV file
simpsons_personaggi_data = pd.read_csv('./simpsons_characters.csv', index_col=False, delimiter=',')
simpsons_personaggi_data = simpsons_personaggi_data.fillna('Null')
print(simpsons_personaggi_data.head(20))

# Fill the table personaggi
for i, row in simpsons_personaggi_data.iterrows():
    sql = "INSERT INTO personaggi VALUES (%s, %s, %s)"
    mycursor.execute(sql, tuple(row))
    print("Record inserted")
    mydb.commit()
