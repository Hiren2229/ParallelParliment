from django.test import TestCase
from . import views
from .models import MembersData, SystemParmeters

# Create your tests here.

class TestModels(TestCase):

	def setUp(self):
		system_param1 = SystemParmeters.objects.create(name='TEST PARAM' , value='XXXX')
		system_param2 = SystemParmeters.objects.create(name='TEST PARAM' , value='YYYYY') #Unique Name required
		system_param3 = SystemParmeters.objects.create(name='TEST PARAM' , value=123)
		system_param4 = SystemParmeters.objects.create(name=123 , value=123)

		member1 = MembersData.objects.create(rec_name = '123_test',
											 member_id = 123,
											 name_list_as = 'test',
											 name_display_as = 'test',
											 name_full_title = 'hiren test',
											 name_address_as = 'hiren Rami',
											 gender = 'Male',
											 thumbnail_url = 'https://www.image.com',
											 official_page_url = 'https://www.Official_url.com',
											 latest_party_id = '1',
											 latest_party_name = 'labout',
											 latest_party_abbreviation = 'labb',
											 latest_party_background_colour = 'aaaaaaa',
											 latest_party_foreground_colour = 'aaaaaaa',
											 latest_party_is_lords_main_party = 'True',
											 latest_party_is_lords_spiritual_party = 'True',
											 latest_party_government_type = 'Test',
											 latest_party_is_independent_party = 'True',
											 latest_house_membership_from = '1',
											 latest_house_membership_from_id = 1,
											 latest_house_membership_house = 1,
											 latest_house_membership_start_date = '23-07-2023 12:00:00.0000',
											 latest_house_membership_end_date = '23-07-2023 12:00:00.0000',
											 latest_house_membership_end_reason = 'XXXXXX',
											 latest_house_membership_end_reason_notes = 'XXXXXX',
											 latest_house_membership_end_reason_id = 'XXXXXX',
											 contact_type = 'XXXXXX',
											 typeDescription = 'XXXXXX',
											 typeId = '14',
											 isPreferred = True,
											 isWebAddress = True,
											 notes = 'XXXXXXXX',
											 line1 = 'XXXXXXXX',
											 line2 = 'XXXXXXXX',
											 postcode = 'NR5 8DS',
											 phone = '082574412285',
											 email = 'hiren@gmail.com')