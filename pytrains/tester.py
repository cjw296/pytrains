from collections import defaultdict
from datetime import datetime
from pytrains.cif.parser import parse

import sys

def main():
    i = 0
    types = defaultdict(int)
    to_print = set(sys.argv[2:])
    try:
        started = datetime.now()
        for message in parse(open(sys.argv[1])):
            types[message.prefix] += 1
            from .cif.meta import ongoing
            if isinstance(message, Exception):
                pass
                #raise message
            elif message.prefix in to_print:
                print '===%s===' % message.__class__.__name__
                for name, value in zip(message._fields, message):
                    print '%20s=%r' % (name, value)
                print
            if not i % 10000:
                print types
            i += 1
    finally:
        duration = datetime.now() - started
        print "%i records in %s at %.0f/s" % (
            i, duration,
            float(i)/duration.seconds if duration.seconds else i
            )
        
if __name__=='__main__':
    main()
