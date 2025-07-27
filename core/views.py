# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def test_api(request):
    return Response({
        "message": "API is working!",
        "status": "ok"
    })

class TestAPI(APIView):
    def get(self, request):
        return Response({"message": "DRF is working!"}, status=status.HTTP_200_OK)