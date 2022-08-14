from dateutil.relativedelta import relativedelta
from datetime import date, datetime

date_now = datetime.now()
date_earlier = datetime.strptime("2000-02-01", "%Y-%m-%d")
dif = relativedelta(date_now, date_earlier).years


def year_dif(base_date: datetime, minus_date: datetime):
    '''
    megadja két dátum között az eltelt évek számát például 2022-08-01--2000-01-01 --> (22 év)
    :param base_date: the date that be substracted
    :param minus_date:the date that represent the substraction value
    :return: the difference between base_date and minus-date in years
    '''
    dif = relativedelta(base_date, minus_date).years

    return dif
