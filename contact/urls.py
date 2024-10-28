from django.urls import path
from .views import contact_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='contact/contact_success.html'), name='contact_success'),
]
