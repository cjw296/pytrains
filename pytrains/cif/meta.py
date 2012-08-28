from collections import namedtuple
from datetime import date, time

class Field(object):
    order = 0
    def __init__(self, size, type=None):
        self.order = self.__class__.order
        self.__class__.order += 1
        self.size = size
        self.type = type

class Generator(object):
    def __init__(self, tupletype, fields):
        self.tupletype = tupletype
        self.fields = fields
    def __call__(self, type, line):
        return self.tupletype(type, *(
            line[i1:i2] if convert is None else convert(line[i1:i2])
            for convert, i1, i2 in self.fields
            ))

class RecordTypeMeta(type):
    def __init__(cls, class_name, bases, fields):
        if class_name=='RecordType':
            return
        specs = []
        for field_name, field_obj in fields.items():
            if isinstance(field_obj, Field):
                specs.append(
                    (field_obj.order, field_obj.size, field_obj.type, field_name)
                    )
        specs.sort()
        generator_fields = []
        tuple_fields = ['prefix']
        index = 2
        for order, size, convert, field_name in specs:
            next_index = index + size
            tuple_fields.append(field_name)
            generator_fields.append((convert, index, next_index))
            index = next_index
        cls.all[cls.prefix] = Generator(
            namedtuple(class_name, tuple_fields),
            generator_fields
            )

class RecordType(object):
    all = {}
    __metaclass__ = RecordTypeMeta

class Constant(object):
    def __init__(self, txt, description):
        self.txt = txt
        self.description = description
    def __repr__(self):
        return '<%s>' % self.description
    
# type convertors
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

class one_of(dict):
    def __init__(self, *options):
        for option in options:
            self[option.txt] = option
    def __call__(self, txt):
        return self[txt]

Days = namedtuple('Days',
                  'monday tuesday wednesday thursday friday saturday sunday')
def days(txt):
    return Days(*map(int, txt))
