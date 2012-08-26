from .meta import Constant, RecordType, Field, ddmmyy, hhmm, one_of

class Unknown(Exception):

    def __init__(self, type, line):
        self.type, self.line = type, line[:-2]

    def __repr__(self):
        return '<%s:%s>' % (self.type, self.line)

    __str__ = __repr__

update = Constant('U', 'update')
full = Constant('F', 'full')

class Header(RecordType):

    prefix = 'HD'
    mainframe_id = Field(20)
    date_of_extract = Field(6, ddmmyy)
    time_of_extract = Field(4, hhmm)
    current_file_ref = Field(7)
    last_file_ref = Field(7)
    update_indicator = Field(1, one_of(update, full))
    version = Field(1)
    start_date = Field(6, ddmmyy)
    end_date = Field(6, ddmmyy)
