from .models import *
from rest_framework import serializers
import datetime

class HNGTaskSerializer(serializers.ModelSerializer):
    status_code = serializers.SerializerMethodField()
    current_day = serializers.SerializerMethodField()
    utc_time = serializers.SerializerMethodField()
    class Meta:
        model = HNGSLack
        fields = ['id', 'slack_name', 'current_day', 'utc_time', 'track', 'github_file_url', 'github_repo_url', 'status_code' ]
        
    def get_status_code(self, obj):
        if HNGSLack.objects.exists():
            return 200
        else:
            return 400
    def get_current_day(self, obj):
        return datetime.date.today().strftime('%A')
    
    def get_utc_time(self, obj):
        return datetime.datetime.utcnow()