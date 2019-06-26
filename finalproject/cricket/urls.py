from django.contrib import admin
from django.urls import path
from cricket.views import SeasonView,MatchDetailsView,LogoutView,LoginView,SighupView,PointsTableView
from django.shortcuts import *

urlpatterns = [

    path("home/",lambda req:redirect('home_html',2019,1),name='start_html'),
    path("", lambda req: redirect('home_html',2019,1)),

    path('home/<int:year>/<int:page>',SeasonView.as_view(),name='home_html'),
    path('home/<int:year>/<int:page>/match/<int:match_id>/<int:choice>',MatchDetailsView.as_view(),name='match_html'),
    path('points_table/<int:year>',PointsTableView.as_view(),name='points_table_html'),

    path('login/',LoginView.as_view(),name='login_html'),
    path('signup/',SighupView.as_view(),name='signup_html'),
    path('logout/',LogoutView.as_view(),name='logout_html'),
]