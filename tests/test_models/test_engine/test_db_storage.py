#!/usr/bin/python3
""""""


import MySQLdb
import unittest


db = MySQLdb.connect("localhost",
                     user='hbnb_test',
                     passwd='hbnb_test_pwd',
                     db='hbnb_test_db')
cur = db.cursor()

class TestGetDataFromTable(unittest.TestCase):
    def test_create_query(self):
        cur.execute("""SELECT count(id) as Cantidad FROM states""")
        rows = cur.fetchall()
        print(rows)
        self.assertAlmostEqual(rows[0][0], 2)
        cur.close()
        db.close()
