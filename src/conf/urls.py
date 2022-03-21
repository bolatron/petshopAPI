from django.urls import include, path

from rest_framework import routers

from apps.petshop.viewsets import TutorViewSet, AnimalViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'animals', AnimalViewSet, basename='Animals')
router.register(r'tutors', TutorViewSet, basename='Tutors')

urlpatterns = [
    path('api/', include(router.urls))
]