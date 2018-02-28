from .models import CompanyList, PalletList
from .serializers import CompanyListSerializer, PalletListSerializer
from rest_framework import generics, pagination

"""
REST API:
    - http://127.0.0.1:8000/showlist/company/
        Show all the lists
    - http://127.0.0.1:8000/showlist/company/34
        Show the company which has "id 34".
    - http://127.0.0.1:8000/showlist/company/?limit=100&offset=400
        Pagination is used to split data into individual pages.
        /?limit=100&offset=400 => show items from "id 401" to "id 500"
"""

class CompanyListCreate(generics.ListAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer
    pagination_class = pagination.LimitOffsetPagination

class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer

class PalletListCreate(generics.ListAPIView):
    queryset = PalletList.objects.all()
    serializer_class = PalletListSerializer
    pagination_class = pagination.LimitOffsetPagination

class PalletRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PalletList.objects.all()
    serializer_class = PalletListSerializer
