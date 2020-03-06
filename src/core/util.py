import datetime
from .models import Remesa

def date_range(start_date, end_date):
    if isinstance(start_date, datetime.datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime.datetime):
        end_date = end_date.date()
    if start_date > end_date:
        raise ValueError('You provided a start_date that comes after the end_date.')
    while True:
        yield start_date
        start_date = start_date + datetime.timedelta(days=1)
        if start_date > end_date:
            break

def remesa(fecha):
    try:
        for rem in Remesa.objects.all():
            if fecha >= rem.inicio and fecha <= rem.fin:
                return rem
    except:
        return None