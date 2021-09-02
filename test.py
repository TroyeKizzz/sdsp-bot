import mysql.connector

mydb = mysql.connector.connect(
  host="mydb.tamk.fi",
  user="cpsvva",
  password="6S52I9So",
  database="dbcpsvva1"
)

mycursor = mydb.cursor()

sql = "INSERT INTO votes (candidate) VALUES ({0})".format(1)
mycursor.execute(sql)

mydb.commit()