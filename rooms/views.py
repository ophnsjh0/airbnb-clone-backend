from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import AmenitiesSerializer, RoomDetailSerializer, RoomListSerializer
from .models import Amenity, Room


# Create your views here.
#
class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitiesSerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitiesSerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitiesSerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitiesSerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitiesSerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_serailizer = serializer.save()
            return Response(
                AmenitiesSerializer(update_serailizer).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# from django.shortcuts import render
# from django.http import HttpResponse+

# def see_all_rooms(request):
#     rooms = Room.objects.all()
#     return render(
#         request,
#         "all_rooms.html",
#         {
#             "rooms": rooms,
#             "title": "Hello! this title comes form django!",
#         },
#     )


# def see_one_room(request, room_pk):
#     try:
#         room = Room.objects.get(pk=room_pk)
#         return render(
#             request,
#             "room_detail.html",
#             {
#                 "room": room,
#             },
#         )
#     except Room.DoesNotExist:
#         return render(
#             request,
#             "room_detail.html",
#             {
#                 "not_found": True,
#             },
#         )
