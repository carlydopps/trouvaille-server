"""trouvaille URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from trouvailleapi.views import register_user, login_user, ExperienceView, ExperienceTypeView, DestinationView, DurationView, SeasonView, StyleView, TravelerView, TripView, TripDestinationView, TripExperienceView, SubscriptionView, CommentView, FavoriteTripView, ImageView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'experiences', ExperienceView, 'experience')
router.register(r'experience_types', ExperienceTypeView,'experience_types')
router.register(r'destinations', DestinationView,'destination')
router.register(r'durations', DurationView,'duration')
router.register(r'seasons', SeasonView,'season')
router.register(r'styles', StyleView,'style')
router.register(r'travelers', TravelerView,'traveler')
router.register(r'trips', TripView,'trip')
router.register(r'trip_destinations', TripDestinationView,'trip_destination')
router.register(r'trip_experiences', TripExperienceView,'trip_experience')
router.register(r'subscriptions', SubscriptionView,'subscription')
router.register(r'comments', CommentView,'comment')
router.register(r'favorite_trips', FavoriteTripView,'favorite_trip')
router.register(r'images', ImageView,'image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]
