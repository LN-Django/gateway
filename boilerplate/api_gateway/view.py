import requests as api_request
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from .external_services import services


class CalculatorView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        service = services['calculator']
        external_response = api_request.post(service.endpoint, headers={
            'Accept': 'application/json'}, json=request.data)

        return Response(external_response.json(), status=external_response.status_code)


class ListProductsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        service = services['list_products']
        external_response = api_request.get(service.endpoint)

        return Response(external_response.json(), status=external_response.status_code)


class ProductInfoView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, product_id, format=None):
        service = services['product_info']
        external_response = api_request.get(
            service.endpoint.replace("{product_id}", str(product_id)))

        return Response(external_response.json(), status=external_response.status_code)
