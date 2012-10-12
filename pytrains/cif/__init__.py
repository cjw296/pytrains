from fixed import Parser, Record, Field, Discriminator, Skip, Constant, one_of

from .convertors import ddmmyy, days, hhmm, yymmdd, safe_int
from .fields import (
    NewDeleteRevises, STPIndicator, BHX, STATUS, CATEGORY, POWER_TYPE,
    OPERATING_CHARACTERISTICS, CLASS, CATERING
    )

class CIF(Parser):
    
    class Header(Record):
        prefix = Discriminator('HD')
        mainframe_id = Field(20)
        date_of_extract = Field(6, ddmmyy)
        time_of_extract = Field(4, hhmm)
        current_file_ref = Field(7)
        last_file_ref = Field(7)
        update_indicator = Field(1, one_of(
            Constant('U', 'update'),
            Constant('F', 'full')
            ))
        version = Field(1)
        start_date = Field(6, ddmmyy)
        end_date = Field(6, ddmmyy)

    class TIPLOCInsert(Record):
        prefix = Discriminator('TI')
        tiploc = Field(7)
        capitals = Field(2, int)
        nalco = Field(6, int)
        nlc_check = Field(1)
        tps_description = Field(26)
        stanox = Field(5, int)
        po_mcp_code = Field(4, int)
        crs = Field(3)
        capri_description = Field(16)

    class Association(Record):
        prefix = Discriminator('AA')
        type = NewDeleteRevises()
        main_uid = Field(6, str)
        associated_uid = Field(6, str)
        start_date = Field(6, yymmdd)
        end_date = Field(6, yymmdd)
        days = Field(7, days)
        category = Field(2, one_of(
            Constant('JJ', 'join'),
            Constant('VV', 'divide'),
            Constant('NP', 'next'),
            empty = Constant('  ', 'empty (not in spec)')
            ))
        date_indication = Field(1, one_of(
            same_day = Constant('S', 'standard (same day)'),
            next_day = Constant('N', 'over next midnight'),
            prev_day = Constant('P', 'over previous midnight'),
            empty = Constant(' ', 'empty (not in spec)')
            ))
        tiploc = Field(7)
        base_loc_suffix = Field(1)
        assoc_loc_suffix = Field(1)
        diagram_type = Field(1)
        association_type = Field(1, one_of(
            passenger = Constant('P', 'passenger use'),
            operating = Constant('O', 'operating use only'),
            empty = Constant(' ', 'empty (not in spec)')
            ))
        spare = Skip(31)
        stp = STPIndicator()

    class BasicSchedule(Record):
        prefix = Discriminator('BS')
        type = NewDeleteRevises()
        train_uid = Field(6)
        date_from = Field(6, yymmdd)
        date_to = Field(6, yymmdd)
        days = Field(7, days)
        bank_holiday_running = BHX()
        status = STATUS()
        category = CATEGORY()
        identity = Field(4)
        headcode = Field(4)
        course_indicator = Skip(1)
        train_service_code = Field(8)
        portion_id = Field(1) # AKA BUSSEC
        power_type = POWER_TYPE()
        timing_load = Field(4) # Not decoded as requires power_type field
        speed = Field(3, safe_int)
        oper_chars = OPERATING_CHARACTERISTICS()
        train_class = CLASS()
        sleepers = Field(1, one_of(
            none = Constant(' ', 'No sleepers'),
            both = Constant('B', 'First & Standard Class'),
            first = Constant('F', 'First Class only.'),
            standard = Constant('S', 'Standard Class only.'),
            ))
        reservations = Field(1, one_of(
            compulsory = Constant('A', 'Seat Reservations Compulsory'),
            bicycle = Constant('E', 'Reservations for Bicycles Essential'),
            recommended = Constant('R', 'Seat Reservations Recommended'),
            possible = Constant('S', 'Seat Reservations possible from any station'),
            empty = Constant(' ', 'empty (not in spec)')
            ))
        connection_indicator = Field(1) # not used
        catering_code = CATERING()
        service_branding = Skip(4) # appears to be always empty
        spare = Skip(1)
        stp = STPIndicator()

