from django.db import models

# Create your models here.
from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.URLField()

    description = models.CharField(
        max_length=150,
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Photo file"


class Vedio(CommonModel):
    file = models.URLField()

    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Vedio file"


# Create your models here.
