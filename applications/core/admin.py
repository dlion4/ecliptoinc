from django.contrib import admin

# Register your models here.
from .models import Division, Position


class PositionInline(admin.StackedInline):
    model = Position
    extra = 0
    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [PositionInline]
    prepopulated_fields = {
        "slug": ("name",),
    }
