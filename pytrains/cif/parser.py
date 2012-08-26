from .meta import RecordType

from .records import Unknown

def parse(stream):
    for line in stream:
        prefix = line[:2]
        handler = RecordType.all.get(prefix, Unknown)
        yield handler(prefix, line)
