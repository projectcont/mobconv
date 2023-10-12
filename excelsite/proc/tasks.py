import proc.valuta
from proc.serializers import ValutaSerializer

#from celery import shared_task
#@shared_task

def getapi():
    print('getapi before ')
    full_json = proc.valuta.get_full_json()
    dict_ = proc.valuta.get_dict_(full_json)
    serialized_data = ValutaSerializer(data=dict_)
    serialized_data.is_valid(raise_exception=True)
    serialized_data.save()
    print('getapi after')