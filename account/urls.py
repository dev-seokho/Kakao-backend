from django.urls import path

from .views import SignUpView, SignInView

urlpatterns = [
	path('', SignUpView.as_view()),
	path('/signin', SignInView.as_view()),
]
