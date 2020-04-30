from django.urls import path

from .views import ProductView, HomeView

urlpatterns = [
    path('/home', HomeView.as_view()),
    path('', ProductView.as_view()),
]
