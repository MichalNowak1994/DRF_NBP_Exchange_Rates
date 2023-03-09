from django.db import IntegrityError
from rest_framework.response import Response
import requests
from rest_framework import status, viewsets, mixins

from djangoProject1 import settings
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class ExchangeRateViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def create(self, request, *args, **kwargs):
        response = requests.get(url=settings.URL)
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch exchange rates.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            data = response.json()
        except ValueError:
            return Response({'error': 'Invalid response from the server.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        for rate in data[0]['rates']:
            try:
                ExchangeRate.objects.create(
                    date=data[0]['effectiveDate'],
                    currency=rate['currency'],
                    code=rate['code'],
                    mid=rate['mid']
                )
            except IntegrityError:
                return Response({'error': 'All datas already in database.'},
                                status=status.HTTP_418_IM_A_TEAPOT)

        return Response({'message': 'Exchange rates saved successfully.'},
                        status=status.HTTP_201_CREATED)
