import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from showlist import models

import pandas as pd

def make_company_list(dflist):
    result = set()
    for df in dflist:
        result = set(list(result) + list(set(df["코드"])))

    return list(result)

def make_pallet_list(dflist):
    result = set()
    for df in dflist:
        result = set(list(result) + list(set(df["유형"])))

    return list(result)

csvlist = [
    '../data/2010-Table 1.csv',
    '../data/2011-Table 1.csv',
    '../data/2012-Table 1.csv',
    '../data/2013-Table 1.csv',
    '../data/2014-Table 1.csv',
    '../data/2015-Table 1.csv',
    '../data/2016-Table 1.csv',
    '../data/2017-Table 1.csv',
]

dflist = []
for csv in csvlist :
    dflist.append(pd.read_csv(csv))

print("----- dflist is prepared! -----")

company_list = make_company_list(dflist)
pallet_list = make_pallet_list(dflist)

print("----- company / pallet list is prepared! -----")

for name in company_list:
    try :
        # check if company code already exists.
        exist = models.CompanyList.objects.get(company=name)

    except :
        # if not, append new company code in the database.
        new_company = models.CompanyList(company=name)
        new_company.save()

for name in pallet_list:
    try :
        # check if company code already exists.
        exist = models.PalletList.objects.get(pallet=name)

    except :
        # if not, append new company code in the database.
        new_pallet = models.PalletList(pallet=name)
        new_pallet.save()

print("----- Saving database is completed! -----")
