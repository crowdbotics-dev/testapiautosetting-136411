from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136411ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136411", Testconnectors136411ViewSet, basename="testconnectors136411"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
