from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rami.models import MembersData

def paginate_data(data, request, records_per_page=20):
    paginator = Paginator(data, records_per_page)
    page = request.GET.get('page')
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)
    return paginated_data

def prepare_data_dict(member_ids):
    return [{'member_id':member.member_id,
                    'name': member.name_display_as,
                    'address': member.name_address_as,
                    'party_name':member.latest_party_name,
                    'membership_house': member.latest_house_membership_house,
                    'email': member.email,
                    'phone': member.phone,
                    'official_page': 'https://members.parliament.uk/member/'+str(member.member_id)+'/contact',
                    'image_url' : member.thumbnail_url
                    } for member in member_ids]

def Mps(request):
    member_ids = MembersData.objects.filter().order_by('member_id')
    member_parties = []
    if member_ids:
        member_parties = (list(set(member_ids.values_list('latest_party_name',flat=True))))
    data_dict = prepare_data_dict(member_ids)
    members = paginate_data(data_dict, request)
    return render(request, 'Mps.html', {'members': members,'member_parties': member_parties})

def member_search(request):
    search_params = request.GET.get('search')
    search_by_party_name = request.GET.get('search_by')
    member_ids = MembersData.objects.filter().order_by('member_id')
    member_parties = []
    if member_ids:
        member_parties = (list(set(member_ids.values_list('latest_party_name',flat=True))))
    if search_params and search_by_party_name != 'name':
        member_ids = MembersData.objects.filter(name_display_as__icontains=search_params,latest_party_name=search_by_party_name).order_by('member_id')
    if search_params == '' and search_by_party_name != 'name':
        member_ids = MembersData.objects.filter(latest_party_name=search_by_party_name).order_by('member_id')
    if search_params != '' and search_by_party_name == 'name':
        member_ids = MembersData.objects.filter(name_display_as__icontains=search_params).order_by('member_id')
    if member_ids:
        data_dict = prepare_data_dict(member_ids)
        members = paginate_data(data_dict, request)
        return render(request, 'Mps.html', {'members': members, 'member_parties': member_parties})
    return render(request, 'Mps.html', {'members': [],'member_parties': member_parties})


def apply_house_filter(request):
    member_ids = MembersData.objects.filter().order_by('member_id')
    member_parties = []
    if member_ids:
        member_parties = (list(set(member_ids.values_list('latest_party_name',flat=True))))
    house_id = request.GET.get('house')
    party_id = request.GET.get('selected_party')
    if party_id != 'name':
        member_ids = MembersData.objects.filter(latest_house_membership_house=house_id,latest_party_name=party_id).order_by('member_id')
    else:
        member_ids = MembersData.objects.filter(latest_house_membership_house=house_id).order_by('member_id')
    data_dict = prepare_data_dict(member_ids)    
    members = paginate_data(data_dict, request)
    return render(request, 'Mps.html', {'members': members,'member_parties': member_parties})    
