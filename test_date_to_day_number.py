import unittest
from date_to_day_number import get_day_of_year

class TestDateToDayNumber(unittest.TestCase):

    def test_valid_date_non_leap_year(self):
        self.assertEqual(get_day_of_year("01-01-2023"), 1)
        self.assertEqual(get_day_of_year("15-06-2023"), 166)
        self.assertEqual(get_day_of_year("31-12-2023"), 365)

    def test_valid_date_leap_year(self):
        self.assertEqual(get_day_of_year("01-01-2024"), 1)
        self.assertEqual(get_day_of_year("29-02-2024"), 60)
        self.assertEqual(get_day_of_year("31-12-2024"), 366)

    def test_invalid_date_format(self):
        error_message = "Invalid date format or value. Please use dd-mm-yyyy."
        self.assertEqual(get_day_of_year("2023-01-01"), error_message)
        self.assertEqual(get_day_of_year("01/01/2023"), error_message)
        self.assertEqual(get_day_of_year("randomstring"), error_message)
        self.assertEqual(get_day_of_year(""), error_message)
        self.assertEqual(get_day_of_year("01-Jan-2023"), error_message)
        self.assertEqual(get_day_of_year("1-1-2023"), error_message) # Needs dd and mm

    def test_invalid_date_value(self):
        error_message = "Invalid date format or value. Please use dd-mm-yyyy."
        self.assertEqual(get_day_of_year("32-01-2023"), error_message) # Day out of range
        self.assertEqual(get_day_of_year("01-13-2023"), error_message) # Month out of range
        self.assertEqual(get_day_of_year("29-02-2023"), error_message) # Feb 29 on non-leap year
        self.assertEqual(get_day_of_year("31-04-2023"), error_message) # April 31 (invalid day for month)
        self.assertEqual(get_day_of_year("00-01-2023"), error_message) # Day zero
        self.assertEqual(get_day_of_year("01-00-2023"), error_message) # Month zero

if __name__ == '__main__':
    unittest.main()
