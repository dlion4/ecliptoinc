from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField, DecimalRangeField
from django.urls import reverse
import datetime
from django.utils import timezone


# Create your models here.
class Division(models.Model):
    name = models.CharField(
        max_length=100, unique=True, help_text="It, Data Science etc"
    )

    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Division, self).save(*args, **kwargs)


class Position(models.Model):
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    positions = models.PositiveIntegerField(default=1)
    requirements = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expiry = models.DateField(auto_now_add=True)
    type = models.CharField(
        max_length=1,
        choices=(
            ("R", "Rmote"),
            ("F", "Full Time"),
            ("C", "Contract"),
            ("I", "Internship"),
        ),
        default="R",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("position", kwargs={"career_slug": self.slug})

    @property
    def salary(self):
        return (
            f"{self.min_salary} - {self.max_salary}"
            if self.min_salary and self.max_salary
            else self.min_salary or self.max_salary
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.expiry += datetime.timedelta(days=45)
        super(Position, self).save(*args, **kwargs)
