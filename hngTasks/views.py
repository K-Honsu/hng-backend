from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView

class HNGTaskViewSet(RetrieveAPIView, GenericAPIView):
    queryset = HNGSLack.objects.all()
    serializer_class = HNGTaskSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)  
