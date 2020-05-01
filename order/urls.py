from django.urls import path

from .views import BasketView

urlpatterns = [
    path('', BasketView.as_view())
]

