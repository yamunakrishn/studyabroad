from django.shortcuts import render

# Create your views here.
#sherry george
def login(request):
    return render(request,'login.html')
def studens(request):
    return render(request,'councilordashboard.html')#studentscouncilor tab
def sales(request):
    return render(request,'salesnewly.html')  
def newlyleades(request):
    return render(request,'newlyleads.html')    
def currentleadss(request):
    return render(request,'currentleads.html') 
def previousleadss(request):
    return render(request,'previouslyassleads.html')      
def previousdash(request):
    return render(request,'itheadpage.html')     
def statuscurrent(request):
    return render(request,'status1.html')      

#dilshad
def dashboard(request):
    return render(request,'dashboard_head.html')    
def team_leader_clints(request):
    return render(request,'clints.html')  
def status_progress(request):
    return render(request, 'status.html')      

# counsilor dashboard
#sambhu
def home(request):
     return render(request,'councilor/home.html')
def currentleads(request):
     return render(request, 'councilor/current_leads.html')
def previousleads(request):
    return render(request, 'councilor/previous_leads.html')
def councilornewlyprofile(request):
    return render(request, 'councilor/councilornewprof.html') 
def status2(request):
    return render(request, 'councilor/counstatus1.html')  
# #eldho    



def newlyassignleads(request):
     return render(request, 'councilor/newly_leads.html')
def status1(request):
    return render(request, 'councilor/counstatus.html')       







    #Attendance

def attendance(request):
    return render(request,'attendance.html')
def addteamlead(request):
    return render(request,'addteamlead.html')
def ithead(request):
    return render(request,'itheadprofile.html')
def currentithead(request):
    return render(request,'currentithead.html')
def previousithead(request):
    return render(request,'previousithead.html')
def documentofficerprofile(request):
    return render(request,'documentofficerprofile.html')
def documentofficers(request):
    return render(request,'documentofficers.html')
def documentofficercard(request):
    return render(request,'documentofficercard.html')
def currentdocoff(request):
    return render(request,'currentdocoff.html')
def previousdocoff(request):
    return render(request,'previousdocoff.html')
def attendancecard(request):
    return render(request,'attendancecard.html')
def attendanceview(request):
    return render(request,'attendanceview.html')
def attendancesearch(request):
    return render(request,'attendancesearch.html')
def studentcouncilorcard(request):
    return render(request,'studentcouncilorcard.html')
def previousstudcounc(request):
    return render(request,'previousstudcounc.html')
def teamprofile(request):
    return render(request,'teamprofile.html')
def previousdocoffprofile(request):
    return render(request,'previousdocoffprofile.html')
def currentdocoffprofile(request):
    return render(request,'currentdocoffprofile.html')



