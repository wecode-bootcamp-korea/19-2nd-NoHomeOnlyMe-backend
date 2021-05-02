from django.urls import path, include

urlpatterns = [
    path("room", include("homes.urls")),
    path('search', include("search.urls")),
    path('user', include("users.urls"))
]