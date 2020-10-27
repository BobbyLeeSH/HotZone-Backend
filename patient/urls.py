from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from patient import views

urlpatterns = [
    path('patients/', views.patient_list),
    path('patients/<int:pk>/', views.patient_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
