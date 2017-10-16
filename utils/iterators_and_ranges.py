import datetime as dt

def generic_range(start, end, step_size=1):
    """Yields values betweeen start and end 
     with given step size apart 
     [start, end[
     """
    while start < end:
        yield start
        start = start + step_size

def gen_dates(start_date:dt.datetime, end_date:dt.datetime, days=1):
    """Yields dates, datetime range"""
    while start_date < end_date:
        yield start_date
        start_date = start_date + dt.timedelta(days=days)

def gen_date_sk_range(start:dt.datetime, end:dt.datetime, days):
    """Yields date_sks"""
    while start < end:
        yield start.strptime("Y%m%d%")
        start = start + dt.timedelta(days=days)

def batcher():
    pass



### Tests ###
import unittest

class Test(unittest.TestCase):
    start_i = 2
    end_i = 7
    start_date = dt.datetime(2001, 7, 30)
    end_date = dt.datetime(2001, 8, 2)

    def test_generic_range(self, start_i=start_i, end_i=end_i):
        [2,3,4,5,6] == list(generic_range(start_i, end_i))
        [2, 4, 6] == list(generic_range(start_i, end_i, 2))
        [] == list(generic_range(start_i, end_i, 10))

        [.1, .2, .3] == list(generic_range(.1, .4, .1))

    def test_gen_dates(self, s=start_date, e=end_date):
        next(gen_dates(s, e)) == dt.datetime(2001, 7, 31)
        [dt.datetime(2001, 7, 30)] == gen_dates(s, e, days=2)

    def test_gen_date_sk_range(self, s=start_date, e=end_date):
        next(gen_dates(s, e)) == 20010731
        [20010730, 20010731, 20010801] == gen_dates(s, e)



if __name__ == '__main__':
    unittest.main()

