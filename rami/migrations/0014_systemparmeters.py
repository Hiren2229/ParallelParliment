# Generated by Django 4.1.3 on 2023-07-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rami', '0013_alter_membersdata_membership_status_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemParmeters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.CharField(max_length=250)),
            ],
        ),
    ]