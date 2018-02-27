# Generated by Django 2.0.2 on 2018-02-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='Unknown', max_length=100)),
            ],
            options={
                'ordering': ('company',),
            },
        ),
        migrations.CreateModel(
            name='PalletList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallet', models.CharField(default='Unknown', max_length=100)),
            ],
            options={
                'ordering': ('pallet',),
            },
        ),
    ]
