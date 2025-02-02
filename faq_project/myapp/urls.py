from django.urls import path
from .views import FAQViewSet, faq_create, faq_delete, faq_update, faq_detail

urlpatterns = [
    path('faqs/', FAQViewSet, name="faq_list"),
    path('faqs/<int:pk>/', faq_detail, name="faq_detail"),
    path('faqs/add/', faq_create, name="faq_create"),
    path('faqs/<int:pk>/update/', faq_update, name="faq_update"),
    path('faqs/<int:pk>/delete/', faq_delete, name="faq_delete"),
]
