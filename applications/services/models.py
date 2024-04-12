from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from typing import ClassVar


class CategoryManager(models.QuerySet):

    def monthly_pricing(self):
        return self.get(category_plan__name__icontains="Monthly")

    def yearly_pricing(self):
        return self.get(category_plan__name="Y")


class AbstrDb(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(AbstrDb, self).save(*args, **kwargs)


class Category(AbstrDb):
    icon = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="category/")

    # objects: ClassVar[CategoryManager] = CategoryManager()
    objects = CategoryManager.as_manager()

    def services(self):
        return self.category_services.all()  # type: ignore

    def monthly_plan(self):
        return self.category_plan.get(name="M")  # type: ignore

    def yearly_plan(self):
        return self.category_plan.get(name="Y")  # type: ignore

    def plans(self):
        return self.category_plan.all()  # type: ignore

    def get_absolute_url(self):
        return reverse("services:category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        return super(Category, self).save(*args, **kwargs)


# Create your models here.
class Service(AbstrDb):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category_services",
    )

    def save(self, *args, **kwargs):
        return super(Service, self).save(*args, **kwargs)


class ServiceVariant(AbstrDb):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_variants"
    )

    def save(self, *args, **kwargs):
        return super(ServiceVariant, self).save(*args, **kwargs)


class Plan(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="category_plan",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        choices=(
            ("M", "Monthly"),
            ("Y", "Yearly"),
        ),
        unique=True,
        default="M",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Plan, self).save(*args, **kwargs)

    def plan_features(self):
        return self.plan.all()  # type: ignore


class Pricing(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plan")
    package = models.CharField(
        max_length=100,
        choices=(
            ("B", "Basic"),
            ("P", "Premium"),
            ("E", "Enterprise"),
        ),
        default="B",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f"{self.plan.name} {self.package}"

    def calculated_discount(self):
        return f"{int((self.discount / self.price) * 100)}"

    def features(self):
        return self.pricing.all()  # type: ignore

    def save(self, *args, **kwargs):
        if self.discount:
            self.discounted_price = self.price - self.discount
        self.discounted_price = self.price
        return super(Pricing, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("plan", "package"),
                name="unique_pricing_plan_package",
            )
        ]


class PricingFeature(models.Model):
    pricing = models.ForeignKey(
        Pricing, related_name="pricing", on_delete=models.CASCADE
    )
    feature = models.CharField(max_length=100)
