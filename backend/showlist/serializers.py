from rest_framework import serializers
from .models import CompanyList, PalletList

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList
        fields = ('id', 'company')

class PalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalletList
        fields = ('id', 'pallet')
