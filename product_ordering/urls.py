from django.contrib import admin
from django.urls import path, include

from shop.views import OrderCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),

]
