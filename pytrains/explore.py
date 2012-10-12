from collections import defaultdict
from datetime import datetime
from fixed import Handler, handles, UnknownRecordType
from pytrains.cif import CIF

import sys

class CIFHandler(Handler):

    lines = 0
    parse_unknown = False
    
    def __init__(self):
        self.lines = 0
        self.types = defaultdict(int)

    @handles(CIF.Association)
    def the_record(self, source, line_no, message):
        self.lines += 1
        #if self.lines % 10000:
        #    print self.types
        #for e in message.catering_code:
        #    self.types[e] += 1
        self.types[message.stp] += 1

def real_main():
    types = defaultdict(int)
    to_print = set(sys.argv[2:])
    try:
        started = datetime.now()
        handler = CIFHandler()
        handler.handle(open(sys.argv[1]))
    finally:
        print handler.types
        duration = datetime.now() - started
        print "%i records in %s at %.0f records/second" % (
            handler.lines, duration,
            float(handler.lines)/duration.seconds if duration.seconds else handler.lines
            )

import cProfile
def main():
    cProfile.runctx("real_main()", globals(), locals(), filename="fixed.profile" )
    import os; print os.getcwd() 
    
if __name__=='__main__':
    main()
