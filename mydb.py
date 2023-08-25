import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", passwd="Password@123")


# Prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE sun")

print("All Done!")