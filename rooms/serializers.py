from rest_framework.serializers import ModelSerializer
from .models import Amenity


class AmenitiesSerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
