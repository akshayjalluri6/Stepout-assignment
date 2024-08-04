from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginAPI, TrainViewSet, StationViewSet, RouteViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'trains', TrainViewSet)
router.register(r'stations', StationViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterViewSet.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
]
