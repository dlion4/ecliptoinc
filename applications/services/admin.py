from django.contrib import admin
from nested_inline.admin import NestedModelAdmin
from .models import Category, Plan
from .inlines import ServiceInline, PricingInline


@admin.register(Category)
class CategoryAdmin(NestedModelAdmin):
    list_display = ("name", "slug")
    inlines = [
        ServiceInline,
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Plan)
class PlanAdmin(NestedModelAdmin):
    list_display = ("name", "category")
    inlines = (PricingInline,)
