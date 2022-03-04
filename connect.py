import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="python",
    user="postgres",
    password="123456")
