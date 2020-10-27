from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from case import views

urlpatterns = [
    path('cases/', views.case_list),
    path('cases/<int:pk>/', views.case_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
