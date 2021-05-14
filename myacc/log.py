import datetime

def log(msg, sevrity='i'):
    if sevrity == 'i' : sev='INFO'
    if sevrity == 'w' : sev='WARN'
    if sevrity == 'e' : sev='ERR '
    print(f"{str(datetime.datetime.utcnow())[0:23]} {sev} {msg}")
