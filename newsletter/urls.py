from django.urls import path
from .views import subscribe, thank_you

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('thank-you/', thank_you, name='thank_you'),
]
