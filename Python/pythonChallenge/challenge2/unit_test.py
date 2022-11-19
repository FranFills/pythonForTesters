import challenge2
import unittest


class calculate_power(unittest.TestCase):

    def test_calculate_power(self):
        self.assertEqual(challenge2.power_of_number(4, 3), 64)


if __name__ == '__main__':
    unittest.main()
