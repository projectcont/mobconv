from datetime import datetime
from pytz import utc
import proc.tasks
from proc.serializers import ValutaSerializer


def getapi():
    '''
    функция, которая выполняется раз в сутки-
    обрачение к внешнему API (курсы валют),
    и запись данных в базу SQL
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

