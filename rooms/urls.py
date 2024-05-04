from django.urls import path
from . import views

urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
    path("amenitiese/", views.Amenities.as_view()),
    path("amenitiese/<int:pk>", views.AmenityDetail.as_view()),
    # path("", views.see_all_rooms),
    # path("<int:room_pk>", views.see_one_room),
]
