from django.urls import path
from . import views

urlpatterns = [
    # Example URL patterns for the detection app
    path('alerts/', views.SnortAlertList.as_view(), name='snort-alerts'),
]
