from datetime import datetime

def ddmmyy_hhmmss(txt):
    return datetime.strptime(txt, '%d/%m/%y %H.%M.%S')
    
def string_set(txt):
    return set(txt.split())
