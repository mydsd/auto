import pymysql
class ConnectDb():
    def __init__(self,host="mysql.testdb.quan007.com",port=3306,user="dataoke2",password="0Ab9v4Ou0PsMk2soMfVk",dbname="dataoke2"):
        config = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "db": dbname,
            "charset": "utf8mb4",
            "cursorclass": pymysql.cursors.DictCursor
        }
        self.connect = pymysql.connect(**config)
    def operational_database(self,sql):
        cur = self.connect.cursor()  #创建游标对象
        cur.execute(sql)     #执行sql语句
        self.connect.commit()
        data = cur.fetchall()  #获取数据
        return data
    def close_db(self):
        self.connect.close()
if __name__ == '__main__':
    sql = "select id from dtk_lingquan_goods where cid = 1 limit 10;"
    data = ConnectDb().operational_database(sql)
    ConnectDb().close_db()
    print(data)