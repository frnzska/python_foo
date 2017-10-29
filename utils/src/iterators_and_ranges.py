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

def gen_date_sk_range(start:dt.datetime, end:dt.datetime, days=1):
    """Yields date_sk"""
    for date in gen_dates(start, end, days):
        yield date.strftime("%Y%m%d")

def batcher():
    pass
