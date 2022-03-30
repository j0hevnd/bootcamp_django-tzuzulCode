from rest_framework.routers import DefaultRouter
from rest_framework import routers

from apps.reviews import viewsets

# router = DefaultRouter
router = routers.SimpleRouter()

router.register(r'', viewsets.ReviewViewSet, basename='review')

urlpatterns = router.urls