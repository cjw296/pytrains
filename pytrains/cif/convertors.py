from collections import namedtuple
from datetime import date, time
from fixed import Constant, one_of

def ddmmyy(txt):
    day = int(txt[:2])
    month = int(txt[2:4])
    year = int(txt[4:])
    if 60 <= year <= 99:
        year += 1900
    else:
        year += 2000
    return date(year, month, day)

ongoing = Constant('999999', 'ongoing')
def yymmdd(txt):
    if txt=='999999':
        return ongoing
    day = int(txt[4:])
    month = int(txt[2:4])
    year = int(txt[:2])
    if 60 <= year <= 99:
        year += 1900
    else:
        year += 2000
    return date(year, month, day)

def hhmm(txt):
    return time(int(txt[:2]), int(txt[2:]))

Days = namedtuple('Days',
                  'monday tuesday wednesday thursday friday saturday sunday')
def days(txt):
    return Days(*map(int, txt))

def safe_int(txt):
    try:
        return int(txt)
    except ValueError:
        return None

class set_of(one_of):

    size_check = False
    
    def __call__(self, text):
        result = set()
        for char in text:
            if char==' ':
                continue
            result.add(self[char])
        return result
