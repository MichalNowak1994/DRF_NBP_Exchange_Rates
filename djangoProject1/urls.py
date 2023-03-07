from django.urls import include, path
from django.contrib import admin
from nbp import urls

urlpatterns = [
    path("nbp/", include(urls)),
    path("admin/", admin.site.urls),

]