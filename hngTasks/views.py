from .filters import HNGFilter
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, GenericAPIView

class HNGTaskViewSet(RetrieveAPIView, GenericAPIView):
    queryset = HNGSLack.objects.all()
    serializer_class = HNGTaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HNGFilter
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)  
