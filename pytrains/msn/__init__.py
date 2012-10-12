from string import strip

from fixed import Parser, Record, Field, Discriminator, Skip, Constant, one_of

from .convertors import ddmmyy_hhmmss, string_set

class MSN(Parser):

    def __iter__(self):
        # nastiness needed because of the insanity of having the 'A'
        # discriminator used twice in the same format!
        self.iterable = iter(self.iterable)
        yield self.Header(self.iterable.next())
        for record in super(MSN, self).__iter__():
            yield record
            
    class Header(Record):
        # lie here: the discriminator is actually 'A' but we handle
        # that manually above
        record_type = Discriminator('_')
        spaces = Skip(29)
        file_spec = Skip(10)
        version = Field(8)
        created = Field(17, ddmmyy_hhmmss)
        spaces2 = Skip(3)
        version_sequence = Field(2)
        
    class StationDetails(Record):
        record_type = Discriminator('A')
        spaces = Skip(4)
        station_name = Field(30, strip)
        cate_type = Field(1, one_of(
            none = Constant('0', 'Not an interchange Point'),
            small = Constant('1', 'Small Interchange Point'),
            medium = Constant('2', 'Medium Interchange Point'),
            large = Constant('3', 'Large Interchange Point'),
            subsidiary = Constant('9', 'A subsidiary TIPLOC'),
            ))
        tiploc = Field(7)
        subsidiary_code = Field(3)
        spaces2 = Skip(3)
        principal_code = Field(3)
        easting = Field(5, int)
        coordinate_type = Field(1, one_of(
            Constant('E', 'Estimated'),
            Constant(' ', 'Actual'),
            ))
        northing = Field(5, int)
        change_time = Field(2, int)
        footnote = Field(2)
        spaces3 = Skip(11)
        region = Field(3)

    class StationAlias(Record):
        record_type = Discriminator('L')
        spaces = Skip(4)
        station_name = Field(30, strip)
        space = Skip(1)
        alias_name = Field(30, strip)

    class RoutingGroup(Record):
        record_type = Discriminator('V')
        spaces = Skip(4)
        group_name = Field(30, strip)
        space = Skip(1)
        stations = Field(40, string_set)

    # the data in the following records is no longer maintained, so
    # they are minimally mapped
    class Groups(Record):
        record_type = Discriminator('G')
        
    class ThreeAlphaCodeUsageDash(Record):
        record_type = Discriminator('-')
    
    class ThreeAlphaCodeUsageSpace(Record):
        record_type = Discriminator(' ')

    class Trailer(Record):
        record_type = Discriminator('Z')
        
    class Trailer3(Record):
        record_type = Discriminator('0')
        
    class Trailer4(Record):
        record_type = Discriminator('M')
        
    class Trailer5(Record):
        record_type = Discriminator('E')
