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


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class Review_DishViewSet(viewsets.ModelViewSet):
    queryset = Review_Dish.objects.all()
    serializer_class = Review_DishSerializer


class Saved_DishViewSet(viewsets.ModelViewSet):
    queryset = Saved_Dish.objects.all()
    serializer_class = Saved_DishSerializer


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
