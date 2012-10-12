from fixed import Field, Constant, one_of
from .convertors import set_of

# commonly used in CIF, put here to save space

class NewDeleteRevises(Field):
    def __init__(self):
        super(NewDeleteRevises, self).__init__(
            size=1,
            convertor=one_of(
                Constant('N', 'new'),
                Constant('D', 'delete'),
                Constant('R', 'revises'),
                ))

class STPIndicator(Field):
    def __init__(self):
        super(STPIndicator, self).__init__(
            size=1,
            convertor=one_of(
                non_overlay = Constant(' ', 'non overlay user'),
                cancel = Constant('C', 'stp cancellation'),
                new = Constant('N', 'new stp (not an overlay)'),
                permanent = Constant('P', 'permanent'),
                overlay = Constant('O', 'stp overlay'),
                ))
    
# fields from Appendix A of the CIF spec

class BHX(Field):
    def __init__(self):
        super(BHX, self).__init__(
            size=1,
            convertor=one_of(
                none = Constant('X', 'Does not run on specified Bank Holiday Mondays.'),
                edinburgh = Constant('E', 'Does not run on specified Edinburgh Holiday dates'),
                glasgow = Constant('G', 'Does not run on specified Glasgow Holiday dates.'),
                empty = Constant(' ', 'empty (not in spec)')
                ))

class STATUS(Field):
    def __init__(self):
        super(STATUS, self).__init__(
            size=1,
            convertor=one_of(
                bus=Constant('B', 'Bus (Permanent).'),
                freight=Constant('F', 'Freight (Permanent - WTT).'),
                passenger=Constant('P', 'Passenger & Parcels (Permanent - WTT).'),
                ship = Constant('S', 'Ship (Permanent).'),
                trip = Constant('T', 'Trip (Permanent).'),
                stp_passenger = Constant('1', 'STP Passenger & Parcels.'),
                stp_freight = Constant('2', 'STP Freight.'),
                stp_trip = Constant('3', 'STP Trip.'),
                stp_ship = Constant('4', 'STP Ship.'),
                stp_bus = Constant('5', 'STP Bus.'),
                empty = Constant(' ', 'empty (not in spec)')
                ))
        
class CATEGORY(Field):
    def __init__(self):
        super(CATEGORY, self).__init__(
            size=2,
            convertor=one_of(
                # Ordinary Passenger Trains
                Constant('OU', 'Unadvertised Ordinary Passenger'),
                Constant('OS', 'Staff Train'),
                Constant('OW', 'Mixed'),
                # Express Passenger Trains
                Constant('XC', 'Channel Tunnel'),
                Constant('XD', 'Sleeper (Europe Night Services)'),
                Constant('XI', 'International'),
                Constant('XR', 'Motorail'),
                Constant('XU', 'Unadvertised Express'),
                # Buses
                # Empty Coaching Stock Trains
                Constant('EE', 'Empty Coaching Stock (ECS)'),
                Constant('EL', 'ECS, London Underground/Metro Service.'),
                Constant('ES', 'ECS & Staff'),
                # Parcels and Postal Trains
                Constant('JJ', 'Postal'),
                Constant('PM', 'Post Office Controlled Parcels'),
                Constant('PP', 'Parcels'),
                Constant('PV', 'Empty NPCCS'),
                # Departmental Trains
                Constant('DD', 'Departmental'),
                Constant('DH', 'Civil Engineer'),
                Constant('DI', 'Mechanical & Electrical Engineer'),
                Constant('DQ', 'Stores'),
                Constant('DT', 'Test'),
                Constant('DY', 'Signal & Telecommunications Engineer'),
                # Light Locomotives
                Constant('ZB', 'Locomotive & Brake Van'),
                Constant('ZZ', 'Light Locomotive'),
                # (Freight Categories currently under review),
                # Railfreight Distribution
                Constant('J2', 'RfD Automotive (Components)'),
                Constant('H2', 'RfD Automotive (Vehicles)'),
                Constant('J3', 'RfD Edible Products (UK Contracts)'),
                Constant('J4', 'RfD Industrial Minerals (UK Contracts)'),
                Constant('J5', 'RfD Chemicals (UK Contracts)'),
                Constant('J6', 'RfD Building Materials (UK Contracts)'),
                Constant('J8', 'RfD General Merchandise (UK Contracts)'),
                Constant('H8', 'RfD European'),
                Constant('J9', 'RfD Freightliner (Contracts)'),
                Constant('H9', 'RfD Freightliner (Other)'),
                # Trainload Freight
                Constant('A0', 'Coal (Distributive)'),
                Constant('E0', 'Coal (Electricity) MGR'),
                Constant('B0', 'Coal (Other) and Nuclear'),
                Constant('B1', 'Metals'),
                Constant('B4', 'Aggregates'),
                Constant('B5', 'Domestic and Industrial Waste'),
                Constant('B6', 'Building Materials (TLF)'),
                Constant('B7', 'Petroleum Products'),
                # Railfreight Distribution (Channel Tunnel),
                Constant('H0', 'RfD European Channel Tunnel (Mixed Business)'),
                Constant('H1', 'RfD European Channel Tunnel Intermodal'),
                Constant('H3', 'RfD European Channel Tunnel Automotive'),
                Constant('H4', 'RfD European Channel Tunnel Contract Services'),
                Constant('H5', 'RfD European Channel Tunnel Haulmark'),
                Constant('H6', 'RfD European Channel Tunnel Joint Venture'),
                # the following appear to actually be in use in the free
                # CIF data provided by ATOC
                underground = Constant('OL', 'London Underground/Metro Service.'),
                passenger = Constant('OO', 'Ordinary Passenger'),
                express = Constant('XX', 'Express Passenger'),
                sleeper = Constant('XZ', 'Sleeper (Domestic)'),
                bus_replacement = Constant('BR', 'Bus - Replacement due to engineering work'),
                bus_wtt = Constant('BS', 'Bus - WTT Service'),
                empty = Constant('  ', 'empty (not in spec)')
                ))

class POWER_TYPE(Field):
    def __init__(self):
        super(POWER_TYPE, self).__init__(
            size=3,
            convertor=one_of(
                d = Constant('D  ', 'Diesel'),
                dem = Constant('DEM', 'Diesel Electric Multiple Unit.'),
                dmu = Constant('DMU', 'Diesel Mechanical Multiple Unit'),
                e = Constant('E  ', 'Electric.'),
                ed = Constant('ED ', 'Electro-Diesel.'),
                eml = Constant('EML', 'EMU plus D, E, ED locomotive.'),
                emu = Constant('EMU', 'Electric Multiple Unit.'),
                epu = Constant('EPU', 'Electric Parcels Unit.'),
                hst = Constant('HST', 'High Speed Train.'),
                lds = Constant('LDS', 'Diesel Shunting Locomotive.'),
                empty = Constant('   ', 'empty (not in spec)')
                ))

class OPERATING_CHARACTERISTICS(Field):
    def __init__(self):
        super(OPERATING_CHARACTERISTICS, self).__init__(
            size=6,
            convertor=set_of(
                b = Constant('B', 'Vacuum Braked.'),
                c = Constant('C', 'Timed at 100 m.p.h.'),
                d = Constant('D', 'DOO (Coaching stock trains).'),
                e = Constant('E', 'Conveys Mark 4 Coaches.'),
                f = Constant('F', 'Trainman (Guard) required.'),
                m = Constant('M', 'Timed at 110 m.p.h.'),
                p = Constant('P', 'Push/Pull train.'),
                q = Constant('Q', 'Runs as required.'),
                r = Constant('R', 'Air conditioned with PA system.'),
                s = Constant('S', 'Steam Heated.'),
                y = Constant('Y', 'Runs to Terminals/Yards as required.'),
                z = Constant('Z', 'May convey traffic to SB1C gauge.'),
                ))

class CLASS(Field):
    def __init__(self):
        both = Constant('B', 'First & Standard seats.')
        convertor = one_of(
                both = both,
                standard = Constant('S', 'Standard class only.'),
                )
        convertor[' '] = both
        super(CLASS, self).__init__(
            size=1,
            convertor=convertor)

class CATERING(Field):
    def __init__(self):
        super(CATERING, self).__init__(
            size=4,
            convertor=set_of(
                buffet = Constant(
                    'C',
                    'Buffet Service.'
                    ),
                first_class_restaurant = Constant(
                    'F',
                    'Restaurant Car available for First Class passengers.'
                    ),
                hot_food = Constant(
                    'H',
                    'Service of hot food available.'
                    ),
                first_class_meal = Constant(
                    'M',
                    'Meal included for First Class passengers.'
                    ),
                wheelchair_reservations = Constant(
                    'P',
                    'Wheelchair only reservations.'
                    ),
                restaurant = Constant(
                    'R',
                    'Restaurant.'
                    ),
                trolley = Constant(
                    'T',
                    'Trolley Service.'
                    ),
                ))
