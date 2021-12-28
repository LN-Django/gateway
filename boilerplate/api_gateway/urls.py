from django.conf.urls import url
from django.urls import path

from .view import CalculatorView, ListProductsView, ProductInfoView

urlpatterns = [
    url('api/calculator', CalculatorView.as_view()),
    path('api/product/<int:product_id>/info',
         ProductInfoView.as_view()),
    url('api/products', ListProductsView.as_view()),
]
