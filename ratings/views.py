from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ratings.serializers import (UserSerializer, RestaurantSerializer,
    ReviewSerializer, DishSerializer, ReviewDishSerializer,
    UserDishSerializer, AllergySerializer, UserAllergySerializer,
    ReviewAllergySerializer, CountrySerializer)
from ratings.models import (User, Restaurant, Review, Country, ReviewAllergy,
    Dish, UserDish, ReviewDish, Allergy, UserAllergy)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAllergyViewSet(viewsets.ModelViewSet):
    queryset = ReviewAllergy.objects.all()
    serializer_class = ReviewAllergySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class ReviewDishViewSet(viewsets.ModelViewSet):
    queryset = ReviewDish.objects.all()
    serializer_class = ReviewDishSerializer


class UserDishViewSet(viewsets.ModelViewSet):
    queryset = UserDish.objects.all()
    serializer_class = UserDishSerializer


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class UserAllergyViewSet(viewsets.ModelViewSet):
    queryset = UserAllergy.objects.all()
    serializer_class = UserAllergySerializer
