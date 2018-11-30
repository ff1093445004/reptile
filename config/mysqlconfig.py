import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='zhangrui', charset='UTF8')
cur = conn.cursor()
cur.execute("SELECT * FROM PRODUCT")
for i in cur:
    print(i)
cur.close()
conn.close()
