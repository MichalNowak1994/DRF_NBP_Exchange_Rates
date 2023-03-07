from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from nbp.models import ExchangeRate


class ExchangeRateSerializer(serializers.Serializer):
    date = serializers.DateField()
    rates = SerializerMethodField()

    class Meta:
        model = ExchangeRate
        fields = ('id', 'date', 'currency', 'code', 'mid')

    def get_rates(self, obj):
        queryset = ExchangeRate.objects.filter(date=obj.date)
        data = queryset.values('currency', 'code', 'mid')
        return data
