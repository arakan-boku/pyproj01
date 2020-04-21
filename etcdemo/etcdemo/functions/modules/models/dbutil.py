import pymysql

"""
共用DBアクセス用クラス　mode!="product"は自動テストモード　
DB更新が必要な時は　mode="product"にする。
"""


class DbUtil:
    def __init__(self, mode=""):
        TESTSERVER = "localhost"
        TESTDB = "bltdb"
        TESTUSER = "bltuser"
        TESTPASSWORD = "bltpass"
        PRODUCTSERVER = "localhost"
        PRODUCTDB = "bltdb"
        PRODUCTUSER = "bltuser"
        PRODUCTPASSWORD = "bltpass"
        self.PRODUCT = "product"

        self.mode = mode
        if(self.mode != self.PRODUCT):
            self.db = pymysql.connect(
                TESTSERVER, TESTUSER, TESTPASSWORD, TESTDB)
        else:
            self.db = pymysql.connect(
                PRODUCTSERVER,
                PRODUCTUSER,
                PRODUCTPASSWORD,
                PRODUCTDB)

    def get_data(self, sql, params=""):
        cursor = self.db.cursor()
        try:
            if(params == ""):
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)
            return cursor.fetchall()
        except BaseException:
            return []

    def put_data(self, sql, params=""):
        cursor = self.db.cursor()
        try:
            if(params == ""):
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)
            if(self.mode == self.PRODUCT):
                self.db.commit()
            return True
        except BaseException:
            self.db.rollback()
            return False

    def do_multi_sql(self, sqllist):
        try:
            for sql in sqllist:
                cursor = self.db.cursor()
                cursor.execute(sql[0], sql[1])
                if(self.mode == self.PRODUCT):
                    self.db.commit()
            return True
        except BaseException:
            self.db.rollback()
            return False

    def __del(self):
        self.db.close()
