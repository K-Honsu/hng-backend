
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .serializers import HNGSerializer

class HNGView(APIView):
    def get(self, request):
        slack_name = request.query_params.get('slack_name', '')
        track = request.query_params.get('track', '')

        current_day = datetime.now().strftime('%A')
        current_utc_time = datetime.utcnow()
        valid_time_window = timedelta(minutes=2)

        # Check if the current UTC time is within +/-2 minutes
        if abs((current_utc_time - datetime.utcnow()).total_seconds()) <= valid_time_window.total_seconds():
            utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        else:
            return Response({'error': 'UTC time is not within the +/-2 minute window.'}, status=status.HTTP_400_BAD_REQUEST)

        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': 'https://github.com/K-Honsu/hng-backend/blob/main/hngTasks/views.py',
            'github_repo_url': 'https://github.com/K-Honsu/hng-backend',
            'status_code': 200
        }

        serializer = HNGSerializer(data=response_data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
