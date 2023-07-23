import requests
from rami.models import MembersData,SystemParmeters
from .utils import create_records_with_additional_fields

def fetch_mp_records():
    member_api_base_url = 'https://members-api.parliament.uk/api/Members/'
    headers = {'accept': 'text/plain'}
    Mps_obj = MembersData()
    lattest_member = MembersData.objects.latest('member_id')
    sys_params = SystemParmeters.objects.filter(name='fetch data limit')[:1]
    member_count = 0
    search_limit = 0
    if lattest_member and lattest_member.member_id:
        member_count = lattest_member.member_id
    if not lattest_member:
        member_count = 0
    if sys_params:
        search_limit = member_count + int(sys_params[0].value)
    try:
        for member_id in range(member_count, search_limit):
            contact_api_url = member_api_base_url+str(member_id)+'/Contact'
            check_commong = Mps_obj.is_commons(member_id)
            official_page_url = 'https://members.parliament.uk/member/'+str(member_id)+'/contact'
            if check_commong == False:
                call_url = member_api_base_url+str(member_id)
                members_response = requests.get(call_url, headers=headers)
                members_contact_res = requests.get(contact_api_url, headers=headers)
                if members_response.status_code == 200:
                    data_dict = members_response.json()['value']
                    contact_data = members_contact_res.json()['value'] if len(members_contact_res.json()['value']) > 0 else {}
                    dict_keys = contact_data.keys() if isinstance(contact_data, dict) else []
                    data_json = data_dict
                    membershi_end_date = data_json['latestHouseMembership']['membershipEndDate']
                    if membershi_end_date != 'null':
                        gender = ''
                        if data_json['gender'] == 'M':
                            gender = 'Male'
                        elif data_json['gender'] == 'F':
                            gender = 'Female'
                        else:
                            gender = 'Other'
                        unque_name = str(data_json['id'])+'_'+data_json['nameListAs'].split(',')[0]
                        member = MembersData.objects.create(
                            rec_name = unque_name,
                            member_id = data_json['id'],
                            name_list_as = data_json['nameListAs'],
                            name_display_as = data_json['nameDisplayAs'],
                            name_full_title =  data_json['nameFullTitle'],
                            name_address_as = data_json['nameAddressAs'] if data_json['nameAddressAs'] else ' ',
                            gender = gender,
                            thumbnail_url = data_json['thumbnailUrl'],
                            latest_party_id = data_json['latestParty']['id'] if data_json['latestParty'] != None else None,
                            latest_party_name = data_json['latestParty']['name'] if data_json['latestParty'] != None else None,
                            latest_party_abbreviation = data_json['latestParty']['abbreviation'] if data_json['latestParty'] != None else None,
                            latest_party_background_colour = data_json['latestParty']['backgroundColour'] if data_json['latestParty'] != None and data_json['latestParty']['backgroundColour'] != None else ' ',
                            latest_party_foreground_colour = data_json['latestParty']['foregroundColour'] if data_json['latestParty'] != None else None,
                            latest_party_is_lords_main_party = data_json['latestParty']['isLordsMainParty'] if data_json['latestParty'] != None else None,
                            latest_party_is_lords_spiritual_party = data_json['latestParty']['isLordsSpiritualParty'] if data_json['latestParty'] != None else None,
                            latest_party_government_type = data_json['latestParty']['governmentType'] if data_json['latestParty'] != None and  data_json['latestParty']['governmentType'] != None else ' ',
                            latest_party_is_independent_party = data_json['latestParty']['isIndependentParty'] if data_json['latestParty'] != None else None,
                            latest_house_membership_from = data_json['latestHouseMembership']['membershipFrom'] if data_json and data_json['latestHouseMembership'] != None else None,
                            latest_house_membership_from_id = data_json['latestHouseMembership']['membershipFromId'] if data_json and data_json['latestHouseMembership'] != None else None,
                            latest_house_membership_house = data_json['latestHouseMembership']['house'] if data_json and data_json['latestHouseMembership'] != None else None,
                            latest_house_membership_start_date = data_json['latestHouseMembership']['membershipStartDate'] if data_json and data_json['latestHouseMembership'] != None else None,
                            latest_house_membership_end_reason_id = data_json['latestHouseMembership']['membershipStatus'] if data_json['latestHouseMembership'] != None and  data_json['latestHouseMembership']['membershipStatus'] != None else ' ',
                            membership_status_is_active = True if data_json['latestHouseMembership']['membershipEndDate'] == 'null' else False,
                            membership_status_notes = data_json['latestHouseMembership']['membershipEndReasonNotes'] if data_json else None,
                            membership_status_description = data_json['latestHouseMembership']['membershipEndReason'] if data_json['latestHouseMembership']['membershipEndReason'] != None else ' ',
                            membership_status_id = data_json['latestHouseMembership']['membershipEndReasonId'] if data_json['latestHouseMembership']['membershipEndReasonId'] != None else 0,
                            membership_status_start_date = data_json['latestHouseMembership']['membershipStartDate'] if data_json else None,
                            contact_type = contact_data['type'] if 'type' in dict_keys else None,
                            typeDescription = contact_data['typeDescription'] if 'typeDescription' in dict_keys else None,
                            typeId =  contact_data['typeId'] if 'typeId' in dict_keys else None,
                            isPreferred =  contact_data['isPreferred'] if 'isPreferred' in dict_keys else None,
                            isWebAddress =  contact_data['isWebAddress'] if 'isWebAddress' in dict_keys else None,
                            notes =  contact_data['notes'] if 'notes' in dict_keys else None,
                            line1 = contact_data['line1'] if 'line1' in dict_keys else None,
                            line2 = contact_data['line2']  if 'line2' in dict_keys else None + contact_data['line5'] if 'line5' in dict_keys else None,
                            postcode = contact_data['postcode']  if 'postcode' in dict_keys else None,
                            phone = contact_data['phone'] if 'phone' in dict_keys else None,
                            email = contact_data['email'] if 'email' in dict_keys else None,
                        )
                        member.save()
                    else:
                        print('Member data not found')
                        continue
                else:
                    print('Unexpected Response')
                    continue
            else:  
                print('Member is already exists in system')
                continue
    except Exception as e:
        print(' Unexpected Error found ',e)
        


