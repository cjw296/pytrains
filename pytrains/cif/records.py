from .meta import Constant, RecordType, Field, ddmmyy, hhmm, one_of, days, yymmdd

class Unknown(Exception):

    def __init__(self, prefix, line):
        self.prefix, self.line = prefix, line[:-2]

    def __repr__(self):
        return '<%s:%s>' % (self.prefix, self.line)

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

class TIPLOCInsert(RecordType):

    prefix = 'TI'
    tiploc = Field(7)
    capitals = Field(2, int)
    nalco = Field(6, int)
    nlc_check = Field(1)
    tps_description = Field(26)
    stanox = Field(5, int)
    po_mcp_code = Field(4, int)
    crs = Field(3)
    capri_description = Field(16)

empty_1 = Constant(' ', 'empty (not in spec)')
empty_2 = Constant('  ', 'empty (not in spec)')

new = Constant('N', 'new')
delete = Constant('D', 'delete')
revise = Constant('R', 'revises')

join = Constant('JJ', 'join')
divide = Constant('VV', 'divide')
next_ = Constant('NP', 'next')

same_day = Constant('S', 'standard (same day)')
next_day = Constant('N', 'over next midnight')
prev_day = Constant('P', 'over previous midnight')

passenger = Constant('P', 'passenger use')
operating = Constant('O', 'operating use only')

non_overlay_assoc = Constant(' ', 'non overlay user')
cancel_assoc = Constant('C', 'stp cancellation of permanent association')
new_assoc = Constant('N', 'new stp association (not an overlay)')
perm_assoc = Constant('P', 'permanent association')
overlay_assoc = Constant('O', 'stp overlay of permanent association')

class Association(RecordType):

    prefix = 'AA'
    type = Field(1, one_of(new, delete, revise))
    main_uid = Field(6, str)
    associated_uid = Field(6, str)
    start_date = Field(6, yymmdd)
    end_date = Field(6, yymmdd)
    dates = Field(7, days)
    category = Field(2, one_of(join, divide, next_, empty_2))
    date_indication = Field(1, one_of(same_day, next_day, prev_day, empty_1))
    tiploc = Field(7)
    base_loc_suffix = Field(1)
    assoc_loc_suffix = Field(1)
    diagram_type = Field(1)
    association_type = Field(1, one_of(passenger, operating, empty_1))
    spare = Field(31)
    stp = Field(1, one_of(non_overlay_assoc, cancel_assoc, new_assoc, perm_assoc, overlay_assoc))
