from rest_framework import serializers
from ratings.models import Restaurant, Review, Review_Dish, Saved_Dish, Allergy, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_staff")


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "date_added", "street_address", "street_address_2",
                  "city", "state", "country", "phone_number", "website", "google_maps_link")


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ("reviewer", "restaurant", "stars", "food_rating", "primary_allergen",
                  "description", "review_date", "up_vote", "down_vote")


class Review_DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review_Dish
        fields = ("dish_name", "modifications", "description", "item_rating")


class Saved_DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saved_Dish
        fields = ("restaurant", "dish_name", "modifications", "notes", "date_added")


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = ("allergy", "severity", "notes")
