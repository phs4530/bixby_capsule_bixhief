import pymysql

con = pymysql.connect(host="localhost", user="root", password="1234",
                      db='bixby', charset='utf8')

cur = con.cursor()

# sql = "select * from customers"
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
num = cur.execute(sql, val)
print('seccese')
con.commit()
# print(num)
#
for i in cur:
  print(i)