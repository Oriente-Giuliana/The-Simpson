import mysql.connector
import pandas as pd

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

# Switch to the database
mycursor.execute("USE THE_SIMPSON")

# Create the table for the second CSV data (doppiatori) if it doesn't exist
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS doppiatori(
    PERSONAGGIO VARCHAR(30),
    `DOPPIATORE ORIGINALE` VARCHAR(30),
    `DOPPIATORE ITALIANO` VARCHAR(30),
    PRIMARY KEY (PERSONAGGIO)
  );""")

# Delete data from the table doppiatori
mycursor.execute("DELETE FROM doppiatori")
mydb.commit()

# Read data from the second CSV file
simpsons_doppiatori_data = pd.read_csv('./simpsons_doppiatori.csv', index_col=False, delimiter=',')
simpsons_doppiatori_data = simpsons_doppiatori_data.fillna('Null')
print(simpsons_doppiatori_data.head(20))

# Fill the table doppiatori
for i, row in simpsons_doppiatori_data.iterrows():
    sql = "INSERT INTO doppiatori VALUES (%s, %s, %s)"
    mycursor.execute(sql, tuple(row))
    print("Record inserted")
    mydb.commit()

# Join the two tables and retrieve the data
mycursor.execute("SELECT * FROM personaggi INNER JOIN doppiatori ON personaggi.nome = doppiatori.PERSONAGGIO")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
