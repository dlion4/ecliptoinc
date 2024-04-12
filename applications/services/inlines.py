from nested_inline.admin import NestedStackedInline

# Register your models here.
from .models import Service, ServiceVariant, Plan, Pricing, PricingFeature


class ServiceVariantInline(NestedStackedInline):
    model = ServiceVariant
    extra = 1
    fk_name = "service"


class ServiceInline(NestedStackedInline):
    model = Service
    extra = 1
    fk_name = "category"
    inlines = [ServiceVariantInline]
    prepopulated_fields = {"slug": ("name",)}


class PricingFeatureInline(NestedStackedInline):
    model = PricingFeature
    extra = 1
    fk_name = "pricing"


class PricingInline(NestedStackedInline):
    model = Pricing
    extra = 1
    fk_name = "plan"
    inlines = [PricingFeatureInline]


