from .models import HNGSLack
from django_filters.rest_framework import FilterSet

class HNGFilter(FilterSet):
    class Meta:
        model = HNGSLack
        fields = {
            'slack_name': ['exact'],
            'track': ['exact'],
        }