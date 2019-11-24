from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    """An enhanced user model"""
    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Restaurant(models.Model):
    """A model to track restaurant info"""    
    USA = 'USA'
    CANADA = 'CA'
    MEXICO = 'MEX'
    COUNTRY_CHOICES = (
        (USA, 'USA'),
        (CANADA, 'Canada'),
        (MEXICO, 'Mexico'),
    )
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date added", default=timezone.now)
    # last_review = models.DateTimeField("last review")
    street_address = models.CharField(max_length=100, default=None, blank=True, null=True)
    street_address_2 = models.CharField(max_length=30, default=None, blank=True, null=True)
    city = models.CharField(max_length=50, default=None, blank=True, null=True)
    state = models.CharField(max_length=2, default=None, blank=True, null=True)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default=USA)
    phone_number = models.CharField(max_length=15, default=None, blank=True, null=True)
    website = models.CharField(max_length=100, default=None, blank=True, null=True)
    google_maps_link = models.CharField(max_length=300, default=None, blank=True, null=True)

    @property
    def latest_review(self):
        return self.review_set.latest('review_date')

    class Meta:
        ordering = ('name',)


class Review(models.Model):
    """A model that tracks restaurant reviews"""
    ZERO_STAR = 0
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5
    STAR_CHOICES = (
        (ZERO_STAR, '0'),
        (ONE_STAR, '1'),
        (TWO_STAR, '2'),
        (THREE_STAR, '3'),
        (FOUR_STAR, '4'),
        (FIVE_STAR, '5'),
    )
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    score = models.IntegerField(default=0) # overall ease of eating there with given allergy
    food_rating = models.IntegerField(default=0) # overall food rating
    description = models.TextField(default=None, blank=True, null=True)
    review_date = models.DateTimeField("review date", default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    class Meta:
        ordering = ('-review_date',)


class ReviewAllergy(models.Model):
    """Table to track allergies at the time of review"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)


class Review_Dish(models.Model):
    """A dish linked to a review"""    
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=50)
    modifications = models.CharField(max_length=300, default=None, blank=True, null=True)
    description = models.CharField(max_length=300, default=None, blank=True, null=True)
    item_rating = models.IntegerField(default=0)

    class Meta:
        ordering = ('dish_name',)


class Saved_Dish(models.Model):
    """A model to track users' saved dishes"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.SET_NULL)
    dish_name = models.CharField(max_length=50)
    modifications = models.CharField(max_length=300, default=None, blank=True, null=True)
    notes = models.CharField(max_length=300, default=None, blank=True, null=True)
    date_added = models.DateTimeField('date added', default=timezone.now)

    class Meta:
        ordering = ('-date_added', 'dish_name')


class Allergy(models.Model):
    """A base list of allergens"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        ordering = ('name')


class UserAllergy(models.Model):
    """A model to track users' individual allergies"""    
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    severity = models.IntegerField(default=0)
    notes = models.CharField(max_length=300, default=None, blank=True, null=True)

    class Meta:
        ordering = ('-severity', 'allergy')
