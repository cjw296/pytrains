from collections import defaultdict
from datetime import datetime
from fixed import Handler
from pytrains.cif import CIF

import sys

def main():
    i = 0
    types = defaultdict(int)
    to_print = set(sys.argv[2:])
    try:
        started = datetime.now()
        for message in CIF(open(sys.argv[1])):
            types[message.__class__.__name__] += 1
            if isinstance(message, Exception):
                pass
                #raise message
            elif message.prefix in to_print:
                print '===%s===' % message.__class__.__name__
                for name, value in zip(message._fields, message):
                    print '%20s=%r' % (name, value)
                print
            if not i % 100000:
                print types
            i += 1
    finally:
        duration = datetime.now() - started
        print "%i records in %s at %.0f records/second" % (
            i, duration,
            float(i)/duration.seconds if duration.seconds else i
            )
        
if __name__=='__main__':
    main()
