from django.urls import path

from .views import MapView, RoomListView

urlpatterns = [
    path('/map', MapView.as_view()),
    path('/list', RoomListView.as_view()),
]