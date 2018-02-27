from .models import CompanyList, PalletList
from .serializers import CompanyListSerializer, PalletListSerializer
from rest_framework import generics

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer

class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyList.objects.all()
    serializer_class = CompanyListSerializer

class PalletListCreate(generics.ListCreateAPIView):
    queryset = PalletList.objects.all()
    serializer_class = PalletListSerializer

class PalletRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PalletList.objects.all()
    serializer_class = PalletListSerializer
