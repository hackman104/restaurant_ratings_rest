"""restaurant_ratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ratings.models import User, Restaurant, Review, Review_Dish, Saved_Dish, Allergy
from rest_framework import routers
from ratings.views import UserViewSet, RestaurantViewSet, ReviewViewSet, Review_DishViewSet, Saved_DishViewSet, AllergyViewSet

# Declare router info
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/restaurants', RestaurantViewSet)
router.register(r'api/reviews', ReviewViewSet)
router.register(r'api/review_dishes', Review_DishViewSet)
router.register(r'api/saved_dishes', Saved_DishViewSet)
router.register(r'api/allergies', AllergyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]
