from collections import defaultdict
from pytrains.cif.parser import parse

import sys

def main():
    i = 0
    types = defaultdict(int)
    for message in parse(open(sys.argv[1])):
        if isinstance(message, Exception):
            raise message
        else:
            print '===%s===' % message.__class__.__name__
            for name, value in zip(message._fields, message):
                print '%20s=%r' % (name, value)
            print
            
if __name__=='__main__':
    main()
