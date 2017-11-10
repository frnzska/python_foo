import unittest
from utils.src.iterators_and_ranges import gen_dates, gen_date_sk_range, generic_range
import datetime as dt

class Test(unittest.TestCase):
    start_i = 2
    end_i = 7
    start_date = dt.date(2001, 7, 30)
    end_date = dt.date(2001, 8, 2)

    def test_generic_range(self, start_i=start_i, end_i=end_i):
        self.assertEqual([2,3,4,5,6], list(generic_range(start_i, end_i)))
        self.assertEqual([2, 4, 6], list(generic_range(start_i, end_i, 2)))
        self.assertEqual([2], list(generic_range(start_i, end_i, 10)))

    def test_gen_dates(self, s=start_date, e=end_date):
        self.assertEqual([dt.date(2001, 7, 30), dt.date(2001, 8, 1)], list(gen_dates(s, e, days=2)))

    def test_gen_date_sk_range(self, s=start_date, e=end_date):
        self.assertEqual([20010730, 20010731, 20010801], list(gen_date_sk_range(s, e)))



if __name__ == '__main__':
    unittest.main()
