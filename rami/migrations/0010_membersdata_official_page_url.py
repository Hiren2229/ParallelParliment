# Generated by Django 4.1.3 on 2023-07-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rami', '0009_membersdata_contact_type_membersdata_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersdata',
            name='official_page_url',
            field=models.URLField(blank=True, null=True, verbose_name='Office Page'),
        ),
    ]