from collections import defaultdict
from datetime import datetime
from fixed import Handler, handles, UnknownRecordType
from pytrains.cif import CIF

import sys

class CIFHandler(Handler):

    def __init__(self):
        self.types = defaultdict(int)

    @handles(CIF.Association)
    #@handles(CIF.Header)
    #@handles(CIF.TIPLOCInsert)
    @handles(UnknownRecordType)
    def count(self, source, line_no, message):
        self.lines = line_no
        self.types[message.__class__.__name__] += 1
        if not (line_no-1) % 100000:
            print self.types

def main():
    i = 0
    types = defaultdict(int)
    to_print = set(sys.argv[2:])
    try:
        started = datetime.now()
        handler = CIFHandler()
        handler.handle(open(sys.argv[1]))
    finally:
        duration = datetime.now() - started
        print "%i records in %s at %.0f/s" % (
            handler.lines, duration,
            float(handler.lines)/duration.seconds if duration.seconds else handler.lines
            )
        
if __name__=='__main__':
    main()
