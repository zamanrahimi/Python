# how to connect Python to mysql
import mysql.connector

con = mysql.connector.connect(
host="localhost", user="root", password="", database="python"
)

cr = con.cursor()



