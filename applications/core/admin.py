from django.contrib import admin

# Register your models here.
from .models import Division, Position, Contact


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "is_read")
    list_filter = ("is_read",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")
    list_per_page = 25

