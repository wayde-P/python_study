import pymysql

mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_user = "admin"
mysql_password = "67GIf2232yuf11"
mysql_db = "asodb"
mysql_charset = "UTF8"
conn = pymysql.connect(host=mysql_host,
                       port=mysql_port,
                       user=mysql_user,
                       password=mysql_password,
                       db=mysql_db,
                       charset=mysql_charset
                       )
cur = conn.cursor()

content = "select content from errors limit 1;"

cur(exec(u"{0:s}".format(content)))
print(content)
cur.close()
conn.close()
