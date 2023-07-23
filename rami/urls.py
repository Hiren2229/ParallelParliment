from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.Mps, name='Mps'),
	path('search/', views.member_search, name='Member Search'),
	path('member/house/filter', views.apply_house_filter, name='House Filter'),

]