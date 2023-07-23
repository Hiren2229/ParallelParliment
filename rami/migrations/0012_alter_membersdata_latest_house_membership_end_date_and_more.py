# Generated by Django 4.1.3 on 2023-07-22 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rami', '0011_alter_membersdata_ispreferred_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersdata',
            name='latest_house_membership_end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Latest House Membership End Date'),
        ),
        migrations.AlterField(
            model_name='membersdata',
            name='latest_house_membership_start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Latest House Membership Start Date'),
        ),
        migrations.AlterField(
            model_name='membersdata',
            name='membership_status_start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Membership Status Start Date'),
        ),
    ]