# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="root",
#   passwd="1234",
#   database="bixby"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

import pymysql

con = pymysql.connect(host="localhost", user="root", password="1234",
                      db='bixby', charset='utf8')

cur = con.cursor()

# sql = "create table sabjill(" \
#       "title varchar(100)," \
#       "content text," \
#       "primary key (title))"

# cur.execute(sql)
# con.commit()
# sql = "insert into sabjill values ('제목','내용')"
# cur.execute(sql)
# con.commit()

sql = "select * from customers"
num = cur.execute(sql)
print(num)

for i in cur:
  print(i)