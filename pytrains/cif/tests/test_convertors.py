from datetime import date, time
from testfixtures import compare
from unittest import TestCase

from ..convertors import (
    Days, ddmmyy, hhmm, days, ongoing, yymmdd
    )

class TestDDMMYY(TestCase):
    
    def test_00(self):
        compare(date(2000, 1, 1), ddmmyy('010100'))
    
    def test_59(self):
        compare(date(2059, 1, 1), ddmmyy('010159'))
    
    def test_60(self):
        compare(date(1960, 1, 1), ddmmyy('010160'))
    
    def test_99(self):
        compare(date(1999, 1, 1), ddmmyy('010199'))

    def test_month(self):
        compare(date(2012, 8, 26), ddmmyy('260812'))

class TestYYMMDD(TestCase):
    
    def test_00(self):
        compare(date(2000, 1, 1), yymmdd('000101'))
    
    def test_59(self):
        compare(date(2059, 1, 1), yymmdd('590101'))
    
    def test_60(self):
        compare(date(1960, 1, 1), yymmdd('600101'))
    
    def test_99(self):
        compare(date(1999, 1, 1), yymmdd('990101'))

    def test_month(self):
        compare(date(2012, 8, 26), yymmdd('120826'))

    def test_ongoing(self):
        self.assertTrue(yymmdd('999999') is ongoing)

class TestHHMM(TestCase):
    
    def test_it(self):
        compare(time(12, 34), hhmm('1234'))
    
class TestDays(TestCase):
    
    def test_monday(self):
        compare(Days(monday=1,
                     tuesday=0,
                     wednesday=0,
                     thursday=0,
                     friday=0,
                     saturday=0,
                     sunday=0),
                days('1000000'))
    
    def test_tuesday(self):
        compare(Days(monday=0,
                     tuesday=1,
                     wednesday=0,
                     thursday=0,
                     friday=0,
                     saturday=0,
                     sunday=0),
                days('0100000'))
    
    def test_wednesday(self):
        compare(Days(monday=0,
                     tuesday=0,
                     wednesday=1,
                     thursday=0,
                     friday=0,
                     saturday=0,
                     sunday=0),
                days('0010000'))
    
    def test_thursday(self):
        compare(Days(monday=0,
                     tuesday=0,
                     wednesday=0,
                     thursday=1,
                     friday=0,
                     saturday=0,
                     sunday=0),
                days('0001000'))
    
    def test_friday(self):
        compare(Days(monday=0,
                     tuesday=0,
                     wednesday=0,
                     thursday=0,
                     friday=1,
                     saturday=0,
                     sunday=0),
                days('0000100'))
    
    def test_saturday(self):
        compare(Days(monday=0,
                     tuesday=0,
                     wednesday=0,
                     thursday=0,
                     friday=0,
                     saturday=1,
                     sunday=0),
                days('0000010'))
    
    def test_sunday(self):
        compare(Days(monday=0,
                     tuesday=0,
                     wednesday=0,
                     thursday=0,
                     friday=0,
                     saturday=0,
                     sunday=1),
                days('0000001'))
    
