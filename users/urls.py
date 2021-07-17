from django.urls import path

from .views import KakaoSignInView

urlpatterns = [
    path('/signin', KakaoSignInView.as_view()),
]