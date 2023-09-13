from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet


class PersonViewSets(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer