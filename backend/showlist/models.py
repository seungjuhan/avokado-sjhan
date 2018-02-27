from django.db import models

class CompanyList(models.Model):
    company = models.CharField(default='Unknown', max_length=100)

    class Meta:
        ordering = ()

class PalletList(models.Model):
    pallet = models.CharField(default='Unknown', max_length=100)

    class Meta:
        ordering = ()
