from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from nbp.models import ExchangeRate


class ExchangeRateSerializer(serializers.Serializer):
    date = serializers.DateField(read_only=True)
    rates = SerializerMethodField()

    class Meta:
        model = ExchangeRate
        fields = ('id', 'date', 'currency', 'code', 'mid')

    def get_rates(self, obj):
        return {'currency': obj.currency, 'code': obj.code, 'mid': obj.mid}
