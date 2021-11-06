import unittest
from check_pwd import check_pwd


class TestSuite(unittest.TestCase):
    def test1(self):
        password = ""
        self.assertFalse(check_pwd(password))

    def test2(self):
        password = "12345678"
        self.assertTrue(check_pwd(password))


if __name__ == '__main__':
    unittest.main()
