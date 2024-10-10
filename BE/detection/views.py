from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SnortAlert
from .serializers import SnortAlertSerializer

class SnortAlertList(APIView):
    def get(self, request):
        alerts = SnortAlert.objects.all()
        serializer = SnortAlertSerializer(alerts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnortAlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
