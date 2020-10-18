from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": (
                    "guests",
                    "beds",
                    "badrooms",
                    "baths",
                ),
            },
        ),
        (
            "Basic Info",
            {
                "classes": ("collapse",),
                "fields": ("name", "description", "country", "address", "price"),
            },
        ),
        (
            "Times",
            {
                "classes": ("collapse",),
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "More About the Spaces",
            {"classes": ("collapse",), "fields": ("amenities", "house_rules")},
        ),
        ("Last Detail", {"classes": ("collapse",), "fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "badrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "roomType",
        "amenities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    """PhotoAdmin Definition"""