# Generated by Django 4.1.3 on 2023-07-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rami', '0010_membersdata_official_page_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersdata',
            name='isPreferred',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='membersdata',
            name='isWebAddress',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
