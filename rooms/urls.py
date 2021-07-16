from django.urls import path

from rooms.views import RoomDetailView

urlpatterns = [
    path("/<int:home_id>", RoomDetailView.as_view()),
]
