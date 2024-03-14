from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by Words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class RatingFilter(admin.SimpleListFilter):

    title = "Rating Filter~!"

    parameter_name = "rating_num"

    def lookups(self, request, model_admin):
        return [
            ("good_rating", "Good_Rating"),
            ("bad_rating", "Bad_Rating"),
        ]

    def queryset(self, request, rating):
        rating_value = self.value()
        if rating_value:
            if rating_value == "good_rating":
                return rating.filter(rating__gt=3)
            else:
                return rating.filter(rating__lte=3)
        else:
            rating


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        RatingFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
