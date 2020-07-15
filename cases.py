from datetime import date, timedelta, datetime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
start_date = date(2020, 3, 20)
end_date = date(2020, 7, 13)