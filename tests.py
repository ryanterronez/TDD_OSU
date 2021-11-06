import unittest
from check_pwd import check_pwd


class TestSuite(unittest.TestCase):
    #  empty string, should fail
    def test1(self):
        password = ""
        self.assertFalse(check_pwd(password))

    # string of length 7, should fail
    def test2(self):
        password = "1234567"
        self.assertFalse(check_pwd(password))


if __name__ == '__main__':
    unittest.main()
