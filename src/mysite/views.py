from rest_framework import viewsets

from mysite.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

