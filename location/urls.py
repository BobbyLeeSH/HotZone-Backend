from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from location import views

urlpatterns = [
    path('locations/', views.location_list),
    path('locations/<int:pk>/', views.location_detail),
    path('locations/search/<str:place>/', views.location_search),
    path('case-locations/', views.case_location_list),
    path('case-locations/<int:pk>', views.case_location_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
