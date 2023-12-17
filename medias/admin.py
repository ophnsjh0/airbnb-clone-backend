from django.contrib import admin
from .models import Photo, Vedio


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Vedio)
class VedioAdmin(admin.ModelAdmin):
    pass
