from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('company/<int:pk>', views.CompanyRetrieveUpdateDestroy.as_view()),
    path('company/', views.CompanyListCreate.as_view()),
    path('pallet/<int:pk>', views.PalletListCreate.as_view()),
    path('pallet/', views.PalletRetrieveUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
