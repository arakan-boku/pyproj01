import unittest


class TestControll(unittest.TestCase):

    def test_upper(self):
        print("Controll")
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
