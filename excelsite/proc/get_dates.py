from datetime import datetime, date, time
from datetime import timedelta

def dates (day_today) :
    '''
    аргумент - заданная дате
    возвращает - также даты "вчера" и  "позавчера" по отношению к заданной
    '''
    if type(day_today) == str:
        day_today = datetime.strptime(day_today, '%Y-%m-%d').date()

    day_yesturday = day_today - timedelta(days=1)
    day_2 = day_today - timedelta(days=2)
    return (day_today, day_yesturday, day_2)