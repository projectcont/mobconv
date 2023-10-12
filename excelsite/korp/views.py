from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from datetime import datetime, date, time
from datetime import timedelta
import proc.valuta
from proc.serializers import ValutaSerializer
from django.http import JsonResponse
from django.shortcuts import redirect
from datetime import datetime, date, time
from proc.kurs import get_context
from proc.get_dates import dates

def kurs(request: HttpRequest, pagetitle='', dayindex=0) -> HttpResponse:
    '''
    функция определяет сегодняшнюю дату
    берез из БД курсы валют на сегодня, вчера и позавчера
    возвращает эти курсы валют в шаблон
    '''
    day0 = date.today()
    #day0 = datetime.strptime('2023-10-07', '%Y-%m-%d').date()
    context=get_context(dayindex,date=day0)

    day_today, day_yesturday, day_2 = dates(day0)
    context['pagetitle']=pagetitle
    context['day_today'] = day_today
    context['day_yesturday'] = day_yesturday
    context['day_2'] = day_2

    return render(request=request, template_name='korp/base.html', context=context)


def update(request: HttpRequest,pagetitle='',) -> JsonResponse:
    '''
        функция запрашивает внешний API с курсами валют и сохраняет в БД
        также возвращает полученный  API с курсами валют
        '''
    try:
        # получает данные по API https://www.cbr-xml-daily.ru/latest.js в json
        full_json = proc.valuta.get_full_json()

        # берет из json только нужные данные, приводит к dict нашей модели
        dict_ = proc.valuta.get_dict_(full_json)

        # сохраняет данные (добавляет строку в БД)
        serialized_data = ValutaSerializer(data=dict_)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
    except ValueError:
        print("API is not accesible")

    return JsonResponse(full_json)


def pageNotFoun(request: HttpRequest, exception):
    return HttpResponseNotFound('Страница ошибка')
