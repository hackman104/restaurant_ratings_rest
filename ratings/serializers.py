from rest_framework import serializers
from ratings.models import Restaurant, Review, Dish, UserDish, ReviewDish, Allergy, User, UserAllergy, Country, ReviewAllergy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email",
                  "is_staff")


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "date_added", "street_address",
                  "street_address_2", "city", "state", "postal_code",
                  "country", "phone_number", "website", "google_maps_link")


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ("reviewer", "restaurant", "score", "description",
                  "review_date", "up_vote", "down_vote")


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "restaurant", "description", "created_on")


class ReviewDishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewDish
        fields = ("review", "dish")


class UserDishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDish
        fields = ("dish", "user", "notes", "modifications", "score",
                  "created_on")


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = ("name", "description")


class UserAllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAllergy
        fields = ("user", "allergy", "severity", "notes")


class ReviewAllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewAllergy
        fields = ("review", "allergy")


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "code")
