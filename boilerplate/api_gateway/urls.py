from django.conf.urls import url

from .view import CalculatorView

urlpatterns = [
    url('api/calculator', CalculatorView.as_view())
]
