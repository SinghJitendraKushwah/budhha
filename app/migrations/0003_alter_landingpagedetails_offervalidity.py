# Generated by Django 3.2.7 on 2021-09-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210928_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpagedetails',
            name='offerValidity',
            field=models.DateField(blank=True, null=True),
        ),
    ]
