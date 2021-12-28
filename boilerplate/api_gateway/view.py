import requests
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from .external_services import services


class CalculatorView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        service = services['calculator']
        external_response = requests.post(service.endpoint, headers={
                                          'Accept': 'application/json'}, json=request.data)

        print(external_response.text)
        return Response(external_response.json(), status=external_response.status_code)
