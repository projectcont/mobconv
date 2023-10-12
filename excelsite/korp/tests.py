from django.test import TestCase
from proc.serializers import ValutaSerializer
from proc.kurs import get_context
import proc.valuta
from decimal import *

class ValidKursTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        listdata=[
                 {'time_create': '2023-10-07', 'usd': 100, 'eur': 110},
                 {'time_create': '2023-10-06', 'usd': 90, 'eur': 80},
                 {'time_create': '2023-10-05', 'usd': 70, 'eur': 65},
        ]
        for i in listdata:
            serialized_data = ValutaSerializer(data=i)
            if serialized_data.is_valid():
                serialized_data.save()



    def test_valute_view(self):
        responce = self.client.get('/korp/0/')
        responce_data=responce
        print("responce_data= ",responce_data, type(responce_data))
        self.assertEqual(responce.status_code,200)


    def test_valute_view(self):
        responce = self.client.get('/korp/1/')
        responce_data=responce
        print("responce_data= ",responce_data, type(responce_data))
        self.assertEqual(responce.status_code,200)


    def test_valute_view(self):
        responce = self.client.get('/korp/2/')
        responce_data=responce
        print("responce_data= ",responce_data, type(responce_data))
        self.assertEqual(responce.status_code,200)


    def test_data_from_db(self):
        context_retrieved = get_context(0,'2023-10-07')
        context_correct = {'title': 'Курс валют на сегодня', 'day': 0, 'comment': '',  'eur': Decimal('110.00'), 'usd': Decimal('100.00'), }
        self.assertEqual(context_retrieved,context_correct)










