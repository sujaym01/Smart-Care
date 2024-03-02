from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from contact_us import views
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter() # amader router
router.register('', views.ContactUsViewSet) # router er antena

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]