import unittest
from .. import dbutil


class TestDbUtil(unittest.TestCase):

    def setUp(self):
        self.db = dbutil.DbUtil()

    def test_select_with_params(self):
        sql = "select * from dummy_items where c_code = %s;"
        result = self.db.get_data(sql, ('C12345',))
        self.assertEqual(len(result), 4)

    def test_select_no_params(self):
        sql = "select * from dummy_items;"
        result = self.db.get_data(sql)
        self.assertEqual(len(result), 10)

    def test_insert(self):
        sql = "insert into dummy_items values(%s, %s, %s, %s, %s, %s, %s);"
        status = self.db.put_data(
            sql,
            ('0',
             'D12345',
             'XXXXXXX',
             'YYYYYY',
             '2019-10-22 16:36:02',
             '2019-10-22 16:36:02',
             '2020-04-01'))
        self.assertEqual(status, True)

    def test_delete(self):
        sql = "delete from dummy_items where id=%s;"
        status = self.db.put_data(sql, ('10',))
        self.assertEqual(status, True)

    def test_multi_sql(self):
        sqllist = [
            ["update dummy_items set c_code='2222' where id=%s;", ('11',)],
            ["update dummy_items set c_code='3333' where id=%s;", ('12',)],
        ]
        status = self.db.do_multi_sql(sqllist)
        self.assertEqual(status, True)

    def test_select_error(self):
        sql = "select * from dummy_not_exists;"
        result = self.db.get_data(sql)
        self.assertEqual(result, [])
    
    def test_put_error(self):
        sql = "delete from dummy_not_exist;"
        status = self.db.put_data(sql)
        self.assertEqual(status, False)

    def test_multi_error(self):
        sqllist = [
            ["update dummy_not_exist set c_code='2222' where id=%s;", ('11',)],
            ["update dummy_not_exist set c_code='3333' where id=%s;", ('12',)],
        ]
        status = self.db.do_multi_sql(sqllist)
        self.assertEqual(status, False)
     

if __name__ == '__main__':
    unittest.main()
