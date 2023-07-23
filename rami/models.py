from django.utils import timezone
from django.db import models

# Create your models here.


class MembersData(models.Model):

    gender_choices = (
            ('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
        )

    rec_name = models.CharField(max_length=100, verbose_name='Unique Name')
    member_id = models.IntegerField(primary_key=True)
    name_list_as = models.CharField(max_length=100, verbose_name="Name List As")
    name_display_as = models.CharField(max_length=100, verbose_name="Name Display As")
    name_full_title = models.CharField(max_length=100, verbose_name="Name Full Title")
    name_address_as = models.CharField(max_length=100, verbose_name="Name Address As")
    gender = models.CharField(choices=gender_choices ,max_length=6, verbose_name="Gender")
    thumbnail_url = models.URLField(verbose_name="Thumbnail URL")
    official_page_url = models.URLField(verbose_name="Office Page", null=True, blank=True)
    
    latest_party_id = models.IntegerField(verbose_name="Latest Party ID", null=True, blank=True)
    latest_party_name = models.CharField(max_length=100, verbose_name="Latest Party Name", null=True, blank=True)
    latest_party_abbreviation = models.CharField(max_length=100, verbose_name="Latest Party Abbreviation", null=True, blank=True)
    latest_party_background_colour = models.CharField(max_length=7, verbose_name="Latest Party Background Colour", null=True, blank=True)
    latest_party_foreground_colour = models.CharField(max_length=7, verbose_name="Latest Party Foreground Colour", null=True, blank=True)
    latest_party_is_lords_main_party = models.BooleanField(verbose_name="Is Lords Main Party", null=True, blank=True)
    latest_party_is_lords_spiritual_party = models.BooleanField(verbose_name="Is Lords Spiritual Party", null=True, blank=True)
    latest_party_government_type = models.CharField(max_length=100, verbose_name="Latest Party Government Type", null=True, blank=True)
    latest_party_is_independent_party = models.BooleanField(verbose_name="Is Independent Party", null=True, blank=True)

    latest_house_membership_from = models.CharField(max_length=100, verbose_name="Latest House Membership From", null=True, blank=True)
    latest_house_membership_from_id = models.IntegerField(verbose_name="Latest House Membership From ID", null=True, blank=True)
    latest_house_membership_house = models.IntegerField(verbose_name="Latest House Membership House", null=True, blank=True)
    latest_house_membership_start_date = models.DateTimeField(default=timezone.now,verbose_name="Latest House Membership Start Date", null=True, blank=True)
    latest_house_membership_end_date = models.DateTimeField(default=timezone.now,null=True, blank=True, verbose_name="Latest House Membership End Date")
    latest_house_membership_end_reason = models.CharField(max_length=100, null=True, blank=True, verbose_name="Latest House Membership End Reason")
    latest_house_membership_end_reason_notes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Latest House Membership End Reason Notes")
    latest_house_membership_end_reason_id = models.CharField(max_length=300, null=True, blank=True, verbose_name="Latest House Membership End Reason ID")


    # Contact Details
    contact_type = models.CharField(max_length=100, null=True) 
    typeDescription = models.CharField(max_length=100, null=True, blank=True)  
    typeId = models.IntegerField(null=True)  
    isPreferred = models.BooleanField(default=False, null=True)
    isWebAddress = models.BooleanField(default=False, null=True)  
    notes = models.CharField(max_length=255, null=True, blank=True)  
    line1 = models.CharField(max_length=255, null=True)  
    line2 = models.CharField(max_length=255, null=True)  
    postcode = models.CharField(max_length=20 , null=True)  
    phone = models.CharField(max_length=20, null=True)  
    email = models.EmailField(max_length=100 , null=True) 


    membership_status_is_active = models.BooleanField(verbose_name="Membership Status Is Active", null=True, blank=True)
    membership_status_description = models.CharField(max_length=100, verbose_name="Membership Status Description", null=True, blank=True)
    membership_status_notes = models.CharField(max_length=400, null=True, blank=True, verbose_name="Membership Status Notes")
    membership_status_id = models.IntegerField(verbose_name="Membership Status ID", null=True, blank=True)
    membership_status_start_date = models.DateTimeField(default=timezone.now, verbose_name="Membership Status Start Date", null=True, blank=True)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.name_display_as


    def is_commons(self, member_id):
        Mps_obj = MembersData()
        is_commns = False
        if member_id:
            obj = MembersData.objects.filter(member_id = member_id).exists()
            if obj:
                is_commns = True
            else:
                is_commns = False
        return is_commns


class SystemParmeters(models.Model):

    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.name