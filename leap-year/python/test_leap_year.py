import unittest
from leap_year import is_leap_year


class LeapYearShould(unittest.TestCase):

    def test_all_years_divisible_by_400_are_leap_year(self):
        # should be True as 2000 is a leap year
        self.assertTrue(is_leap_year(2000))
        # should be False as 1600 is not a leap year
        self.assertTrue(is_leap_year(1600))


if __name__ == '__main__':
    unittest.main()
