import mysql.connector

# TODO.: Find our own mysql password. Whoops.

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb) 