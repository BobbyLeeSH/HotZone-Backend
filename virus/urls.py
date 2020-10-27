from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from virus import views

urlpatterns = [
    path('virus/', views.virus_list),
    path('virus/<int:pk>/', views.virus_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
