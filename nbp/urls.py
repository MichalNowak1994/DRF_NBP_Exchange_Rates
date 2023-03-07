from django.urls import include, path
from rest_framework import routers
from nbp.views import ExchangeRateViewSet

router = routers.DefaultRouter()
router.register(r'exchange_rates', ExchangeRateViewSet, basename='exchange_rate')


urlpatterns = [
    path('', include(router.urls)),
    path('nbp-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]