import unittest
from main import process


class TestMain(unittest.TestCase):

    def test_1(self):
        expression = 'four(times(five()))'
        self.assertEqual(process(expression), 20)

    def test_2(self):
        expression = 'one(plus(one()))'
        self.assertEqual(process(expression), 2)

    def test_3(self):
        expression = 'seven(minus(three()))'
        self.assertEqual(process(expression), 4)

    def test_4(self):
        expression = 'nine(divided_by(three()))'
        self.assertEqual(process(expression), 3)

if __name__ == '__main__':
    unittest.main()