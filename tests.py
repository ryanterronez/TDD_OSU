import unittest
from check_pwd import check_pwd


class TestSuite(unittest.TestCase):
    #  empty string, should fail
    def test1(self):
        password = ""
        self.assertFalse(check_pwd(password))

    # 8 character string, should pass
    def test2(self):
        password = "12345678"
        self.assertTrue(check_pwd(password))

    # 21 character string, should fail
    def test3(self):
        password = "123451234512345123451"
        self.assertFalse(check_pwd(password))


if __name__ == '__main__':
    unittest.main()
