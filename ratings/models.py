from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):
    """An enhanced user model"""
    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)


class Restaurant(models.Model):
    """A model to track restaurant info"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date added", default=timezone.now)
    # last_review = models.DateTimeField("last review")
    street_address = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    street_address_2 = models.CharField(
        max_length=30, default=None, blank=True, null=True)
    city = models.CharField(max_length=50, default=None, blank=True, null=True)
    state = models.CharField(max_length=2, default=None, blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    postal_code = models.CharField(
        max_length=9, default=None, blank=True, null=True)
    phone_number = models.CharField(
        max_length=15, default=None, blank=True, null=True)
    website = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    google_maps_link = models.CharField(
        max_length=300, default=None, blank=True, null=True)

    @property
    def latest_review(self):
        return self.review_set.latest('review_date')

    class Meta:
        ordering = ('name',)


class Review(models.Model):
    """A model that tracks restaurant reviews"""
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    # overall ease of eating there with given allergy
    score = models.IntegerField(default=0)
    description = models.TextField(default=None, blank=True, null=True)
    review_date = models.DateTimeField("review date", default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    class Meta:
        ordering = ('-review_date',)


class ReviewAllergy(models.Model):
    """Table to track allergies at the time of review"""
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    description = models.CharField(
        max_length=300, default=None, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("name",)


class UserDish(models.Model):
    """A dish/user junction"""
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    notes = models.CharField(max_length=200)
    modifications = models.CharField(
        max_length=300, default=None, blank=True, null=True)
    score = models.IntegerField(default=None, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)


class ReviewDish(models.Model):
    """A dish linked to a review"""
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)


class Allergy(models.Model):
    """A base list of allergens"""
    name = models.CharField(max_length=50)
    description = models.CharField(
        max_length=100, default=None, blank=True, null=True)

    class Meta:
        ordering = ('name',)


class UserAllergy(models.Model):
    """A model to track users' individual allergies"""
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    severity = models.IntegerField(default=0)
    notes = models.CharField(
        max_length=300, default=None, blank=True, null=True)

    class Meta:
        ordering = ('-severity', 'allergy')
