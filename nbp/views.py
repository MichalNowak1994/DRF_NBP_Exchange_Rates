from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, viewsets, mixins
from djangoProject1 import settings
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class ExchangeRateViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
        except ValueError:
            return Response({'error': 'Invalid input data.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if 'rates' not in data or 'effectiveDate' not in data:
            return Response({'error': 'Missing required fields in input data.'},
                            status=status.HTTP_400_BAD_REQUEST)

        for rate in data['rates']:
            try:
                ExchangeRate.objects.create(
                    date=data['effectiveDate'],
                    currency=rate['currency'],
                    code=rate['code'],
                    mid=rate['mid']
                )
            except IntegrityError:
                return Response({'error': 'All data already in database.'},
                                status=status.HTTP_418_IM_A_TEAPOT)

        return Response({'message': 'Exchange rates saved successfully.'},
                        status=status.HTTP_201_CREATED)


class LatestCurrencyRateDateAPIView(generics.GenericAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def get(self, request, *args, **kwargs):
        try:
            latest_date = self.queryset.latest('date').date
            return Response({'A': latest_date})
        except:
            return Response({'A': "2023-04-01"})
