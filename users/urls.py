from django.urls import path

from .views import SignInView, SignUpView, KakaoSocialView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/kakao/login', KakaoSocialView.as_view()),
]