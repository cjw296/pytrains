from fixed import Parser, Record, Field, Discriminator, Skip, Constant, one_of

from .convertors import ddmmyy, days, hhmm, yymmdd

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
        type = Field(1, one_of(
            Constant('N', 'new'),
            Constant('D', 'delete'),
            Constant('R', 'revises'),
            ))
        main_uid = Field(6, str)
        associated_uid = Field(6, str)
        start_date = Field(6, yymmdd)
        end_date = Field(6, yymmdd)
        dates = Field(7, days)
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
        spare = Field(31)
        stp = Field(1, one_of(
            non_overlay = Constant(' ', 'non overlay user'),
            cancel = Constant('C', 'stp cancellation of permanent association'),
            new = Constant('N', 'new stp association (not an overlay)'),
            permanent = Constant('P', 'permanent association'),
            overlay = Constant('O', 'stp overlay of permanent association'),
            ))
