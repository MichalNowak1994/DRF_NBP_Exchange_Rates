from django.urls import path, include
from nbp.views import ExchangeRateViewSet, LatestCurrencyRateDateAPIView

urlpatterns = [
    path('nbp-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('exchange_rates/', ExchangeRateViewSet.as_view({'get': 'list', 'post': 'create'}), name='exchange_rate'),
    path('get_latest_date/', LatestCurrencyRateDateAPIView.as_view(), name='get_latest_date'),
]
