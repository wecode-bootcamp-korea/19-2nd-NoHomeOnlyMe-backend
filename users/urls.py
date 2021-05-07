from django.urls import path

from .views import (KakaoSocialView, LikeView, SignInView, SignUpView)

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/kakao/login', KakaoSocialView.as_view()),
    path("/like", LikeView.as_view())
]