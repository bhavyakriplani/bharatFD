from django.urls import path
from .views import FAQListCreateView, FAQDetailView

urlpatterns = [
    path('api/faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('api/faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]