from django.urls import path,re_path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name='login'),
    path('studens',views.studens, name='studens'),
    path('sales',views.sales, name='sales'),
    path('newlyleades',views.newlyleades,name='newlyleades'),
    path('currentleadss',views.currentleadss,name='currentleadss'),
    path('previousleadss',views.previousleadss,name='previousleadss'),
    path('previousdash',views.previousdash,name='previousdash'),
    path('statuscurrent',views.statuscurrent,name='statuscurrent'),
    #dilashad
    path('dashboard',views.dashboard, name='dashboard' ),
    path('team_leader_clints',views.team_leader_clints,name='team_leader_clints'),
    path('status_progress',views.status_progress,name='status_progress'),

   
    # # Eldho Mathew
   
    path('newlyassignleads',views.newlyassignleads, name='newlyassignleads' ),
    path('status1',views.status1, name='status1' ),
    # # Sambhu v pillai
    path('home',views.home, name='home' ),
    path('currentleads',views.currentleads, name='currentleads' ),
    path('previousleads',views.previousleads, name='previousleads' ),
    path('councilornewlyprofile',views.councilornewlyprofile,name='councilornewlyprofile'),
    path('status2',views.status2, name='status2' ),

    

    ## Attendance
    path('attendance',views.attendance,name='attendance'),
    path('attendancecard',views.attendancecard,name='attendancecard'),
    path('addteamlead',views.addteamlead,name='addteamlead'),
    path('ithead',views.ithead, name='ithead'),
    path('currentithead',views.currentithead,name='currentithead'),
    path('previousithead',views.previousithead,name='previousithead'),
    path('documentofficerprofile',views.documentofficerprofile,name='documentofficerprofile'),
    path('documentofficers',views.documentofficers,name='documentofficers'),
    path('currentdocoff',views.currentdocoff,name='currentdocoff'),
    path('attendanceview',views.attendanceview,name='attendanceview'),
    path('attendancesearch',views.attendancesearch,name='attendancesearch'),
]