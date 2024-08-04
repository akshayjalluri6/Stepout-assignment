from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Train, Station, Route, Booking
from .serializers import UserSerializer, RegisterSerializer, TrainSerializer, StationSerializer, RouteSerializer, BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

#Register API
class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
#Login API
class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.pk,
            "email": user.email
        })


#Train Viewset
class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_classes = [permissions.IsAuthenticated]
    serializer_class = TrainSerializer

#Station Viewset
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_classes = [permissions.IsAuthenticated]
    serializer_class = StationSerializer

#Route Viewset
class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RouteSerializer

# Booking Viewset
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer