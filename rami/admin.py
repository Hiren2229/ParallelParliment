from django.contrib import admin
from . models import MembersData,SystemParmeters
# Register your models here.



class MembersDataAdmin(admin.ModelAdmin):
    readonly_fields =  [field.name for field in MembersData._meta.get_fields()]
    search_fields = ['name_display_as']
    fieldsets = (
        ('Details', {
            'fields': ('rec_name', 'member_id', 'name_list_as', 'name_display_as', 'name_full_title',
                       'name_address_as', 'gender', 'thumbnail_url', 'latest_party_id', 'latest_party_name', 'latest_party_abbreviation'
                       , 'latest_party_background_colour', 'latest_party_foreground_colour',
                        'latest_party_is_lords_main_party',
                        'latest_party_is_lords_spiritual_party',
                        'latest_party_government_type',
                        'latest_party_is_independent_party',
                        'latest_house_membership_from',
                        'latest_house_membership_from_id',
                        'latest_house_membership_house',
                        'latest_house_membership_start_date',
                        'latest_house_membership_end_date',
                        'latest_house_membership_end_reason',
                        'latest_house_membership_end_reason_notes',
                        'latest_house_membership_end_reason_id')
        }),
        ('Contact Details', {
            'fields': ('contact_type', 'typeDescription', 'typeId', 'isPreferred', 'isWebAddress',
                       'notes', 'line1', 'line2', 'postcode', 'phone', 'email')
        }),
    )
    
    list_filter = ('member_id', 'name_list_as', 'latest_party_name','latest_house_membership_house')

admin.site.register(MembersData, MembersDataAdmin)
admin.site.register(SystemParmeters)