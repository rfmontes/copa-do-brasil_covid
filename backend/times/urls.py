from django.urls import path, include

from times.views import TimeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'times', TimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]