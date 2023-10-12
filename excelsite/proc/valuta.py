import requests


def get_full_json():
    # получает данные по API https://www.cbr-xml-daily.ru/latest.js в json
    url = 'https://www.cbr-xml-daily.ru/latest.js'
    response = requests.request("GET", url)
    result = response.json()
    return result


def get_dict_(data):
    '''
    Функция берет из полного json только нужные данные, приводит к dict формата нашей модели
    arg: полный json, полученный от внешнего API
    return:  dict соответствующий формату модели в БД
    '''

    kurs_usd = data['rates']['USD']
    kurs_eur = data['rates']['EUR']
    kurs_usd = round(1/kurs_usd, 2)
    kurs_eur = round(1 / kurs_eur, 2)

    dict_ = {
            'time_create': data.get('date'),
            'usd': kurs_usd,
            'eur': kurs_eur,
        }
    return dict_
