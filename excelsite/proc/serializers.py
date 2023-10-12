from rest_framework import serializers
from korp.models import Valuta


class ValutaSerializer(serializers.ModelSerializer):
    '''
    class ValutaSerializer(serializers.Serializer):
    rate = serializers.CharField(max_length=20)
    DateFrom = serializers.DateTimeField(write_only=True, source='date')
    usd = serializers.CharField(write_only=True, source='USD')
    eur = serializers.CharField(write_only=True, source='EUR')
    kgs = serializers.CharField(write_only=True, source='KGS')
    '''

    class Meta:
        model = Valuta
        fields = ('time_create', 'time_write','usd', 'eur',)
        #fields = '__all__'





