from datetime import datetime

def getCurrTime():
    now = datetime.today()
    now: str = str(now.strftime("%I:%M:%S:%f %p"))
    return now
