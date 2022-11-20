import lesson27
import unittest


class testBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(lesson27.addition(5, 2), 7)
        self.assertNotEqual(lesson27.addition(5, 2), 9)

    def test_subtraction(self):
        self.assertEqual(lesson27.subtraction(5, 2), 3)
        self.assertNotEqual(lesson27.subtraction(5, 2), 7)

if __name__ == '__main__':
    unittest.main()