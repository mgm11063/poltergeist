from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer


class Activities(APIView):
    def get(self, request):
        all_activity = Activity.objects.all()
        serializer = ActivitySerializer(all_activity, many=True)
        return Response(serializer.data)
