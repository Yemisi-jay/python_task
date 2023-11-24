import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "oluwayemisi",
    password = "12345678"
)

print(mydb)
