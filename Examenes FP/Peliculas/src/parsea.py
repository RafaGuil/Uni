from datetime import *

def parsea_date(release_date):
    return datetime.strptime(release_date, "%Y-%m-%d").date()
