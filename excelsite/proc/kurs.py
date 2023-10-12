from korp.models import Valuta
from proc.get_dates import dates

def get_context(dayindex:str,date) -> dict:
    '''
    аргументы:
    - dayindex (0,1,2) : указывает,  показывать ли страницу для  "сегодня"  "вчера"  или "позавчера"
    (определяется параметром в URL)
    - date: дата которая является "сегодняшней"
    возвращает: dict  (курсы валют EUR USD, заголовой, дату, комментарий)
    '''

    day = int(dayindex)

    comment = ''
    day_today,day_yesturday,day_2=dates(date)
    print(dates(date))

    if day == 0:
        title = 'Курс валют на сегодня'
        try:
            valuta = Valuta.objects.filter(time_create=day_today)[0]
            usd = round(valuta.usd, 2)
            eur = round(valuta.eur, 2)
        except IndexError as e:
            usd = eur = ''
            comment = 'Данных на сегодня из API нет'


    if day == 1:
        title = 'Курс валют на вчера'
        try:
            valuta = Valuta.objects.filter(time_create=day_yesturday)[0]
            usd = round(valuta.usd, 2)
            eur = round(valuta.eur, 2)
        except IndexError as e:
            usd = eur = ''
            comment = 'Данных на вчера из API нет'


    if day == 2:
        try:
            title='Курс валют на позавчера'
            valuta = Valuta.objects.filter(time_create=day_2)[0]
            usd = round(valuta.usd, 2)
            eur = round(valuta.eur, 2)
        except IndexError as e:
            usd = eur = ''
            comment = 'Данных на позавчера из API нет'


    context = {'title': title, 'day': day, 'comment': comment,
               'eur': eur, 'usd': usd,}


    return context
