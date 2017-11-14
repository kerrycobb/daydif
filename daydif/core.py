import sys
import datetime

def parse_date(i):
    try:
        year, month, day = i.split('-')
        date = datetime.date(int(year), int(month), int(day))
        return (date)
    except ValueError:
        print ('Error while parsing date')
        print ('Required date format is yyyy-mm-dd')
        sys.exit()

def daydif(startdate, enddate=None):
    startdate = parse_date(startdate)
    if enddate:
        enddate = parse_date(enddate)
    else:
        enddate = datetime.date.today()
    days = (enddate - startdate).days
    return (days)
