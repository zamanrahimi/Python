import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="python",
    user="postgres",
    password="123456")

cr = conn.cursor()
cr.execute("create table emp3 (id int, name text);")
conn.commit()