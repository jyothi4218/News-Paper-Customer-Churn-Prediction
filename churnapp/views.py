from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from .utils import get_newspaper_data
import numpy as np
import pickle
import os
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from .models import UserProfile
import datetime


model_path = os.path.join(settings.BASE_DIR,'models','model.pkl')
# lable encoding
gen_p = os.path.join(settings.BASE_DIR,'models','gender.pkl')
# Reason_p = os.path.join(settings.BASE_DIR,'models','Reason_For_Switch.pkl')
Sub_p = os.path.join(settings.BASE_DIR,'models','Subscription_Type.pkl')
model = pickle.load(open(model_path,'rb'))
g_le = pickle.load(open(gen_p,'rb'))
# r_le= pickle.load(open(Reason_p,'rb'))
s_le= pickle.load(open(Sub_p,'rb'))

# scalling:

age_p = os.path.join(settings.BASE_DIR,'models','age.pkl')
complaints_p =  os.path.join(settings.BASE_DIR,'models','complaints.pkl')
satisfaction_p = os.path.join(settings.BASE_DIR,'models','satisfaction.pkl')
adays = os.path.join(settings.BASE_DIR,'models','Active_Days_Per_Week.pkl')
drt_p = os.path.join(settings.BASE_DIR,'models','Daily_Read_Time.pkl')
ten_p = os.path.join(settings.BASE_DIR,'models','tenure.pkl')


age_s = pickle.load(open(age_p,'rb'))
com_s = pickle.load(open(complaints_p,'rb'))
sat_s = pickle.load(open(satisfaction_p,'rb'))
aday_s = pickle.load(open(adays,'rb'))
drt_s = pickle.load(open(drt_p,'rb'))
ten_s = pickle.load(open(ten_p,'rb'))




def home(request):
    return render (request,'home.html')
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
    return render(request,'login.html')
def registerpage(request):

    if request.method == 'POST':
        email = request.POST.get('num4')
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        conform = request.POST.get('num3')
        if password != conform:
            return render(request,'register.html',{'result':'ERROR'})
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        user=User.objects.create_user(username=username,password=password)
        # Save age and gender
        UserProfile.objects.create(user=user, date= date, gender=gender)
        return redirect('login')
    return render(request,'register.html')

@login_required
def main(request):
    if request.user.is_staff:
        return redirect('churn')  # send admin to churn page
    
    api_key = 'efe868e8436e4325960f9c64b508fcf9'  # Make sure your key is valid
    url = f"https://newsapi.org/v2/everything?q=indian-express&language=en&apiKey={api_key}"
    response = requests.get(url)
    
    try:
        data = response.json()
        articles = data.get('articles', [])
    except Exception as e:
        articles = []
        print("Error fetching news:", e)

    return render(request, 'main.html', {
        'paper_name': 'Indian Express',
        'articles': articles
    })


def switchpage(request):
    newspapers = get_newspaper_data()
    return render(request, 'switchpage.html', {
        'newspapers': newspapers
    })


def conpro(request):
    if request.method == 'POST':
        selected_paper = request.POST.get('selected_paper')
        switch_reason = request.POST.get('switch_reason')
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                profile.reason_for_switch = switch_reason
                profile.save()
            except UserProfile.DoesNotExist:
                pass
        newspapers = get_newspaper_data()

        previous = newspapers.get("indianexpress")
        selected = newspapers.get(selected_paper)

        return render(request, 'conpro.html', {
            'previous_name': previous['name'],
            'selected_name': selected['name'],
            'previous_pros': previous['pros'],
            'selected_cons': selected['cons']
        })
    return redirect('switchpage')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def is_admin(user):
    return user.is_staff

from django.http import JsonResponse
from django.utils.timezone import now

@user_passes_test(lambda u: u.is_staff)
def get_user_details(request):
    user_id = request.GET.get('selected_user')
    try:
        profile = UserProfile.objects.select_related('user').get(user__id=user_id)
        dob = profile.date
        today = now().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        # reason = None
        # if profile.reason_for_switch :
        #     reason = profile.reason_for_switch
        # else:
        #     reason = "Not Switching"

        return JsonResponse({
            'gender': profile.gender,
            'age': age,
            # 'reason':reason
            
        })
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def churn(request):
    prediction = None
    selected_user_id = request.GET.get('selected_user')  # optional support

    users = UserProfile.objects.select_related('user')
    age = ""
    gender = ""
    reason_from_profile = ""
    
    users = UserProfile.objects.select_related('user')

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            age = profile.age
            gender = profile.gender
            # reason_from_profile = profile.reason_for_switch or "Not Switching"
        except UserProfile.DoesNotExist:
            pass
    

    if request.method == 'POST':
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        SubscriptionType = request.POST.get('subscription_type')
        TenureMonths= int(request.POST.get('tenure'))
        DailyReadTime = float(request.POST.get('daily_read_time'))
        ActiveDaysPerWeek= int(request.POST.get('active_days'))
        SatisfactionScore = int(request.POST.get('satisfaction'))
        ComplaintsLast3Months = int(request.POST.get('complaints'))
        # ReasonForSwitch = request.POST.get('reason')
    
        # r_en = r_le.transform([ReasonForSwitch])[0]
        s_en = s_le.transform([SubscriptionType])[0]
        g_en = g_le.transform([gender])[0]
        # if request.user.is_authenticated:
        #     try:
        #         profile = UserProfile.objects.get(user=request.user)
        #         if not profile.reason_for_switch:
        #             profile.reason_for_switch = ReasonForSwitch
        #             profile.save()
        #     except UserProfile.DoesNotExist:
        #         pass

        
        age1 = age_s.transform([[age]])[0][0]
        compleint = com_s.transform([[ComplaintsLast3Months]])[0][0]
        satis = sat_s.transform([[SatisfactionScore]])[0][0]
        aday = aday_s.transform([[ActiveDaysPerWeek]])[0][0]
        drt = drt_s.transform([[DailyReadTime]])[0][0]
        tenu = ten_s.transform([[TenureMonths]])[0][0]

        data=np.array([[age1,g_en,s_en,tenu,drt,aday,satis,compleint]])
        prediction=model.predict(data)
        
    return render(request,'churn.html',{'users':users,'prediction':prediction,'age': age,
        'gender': gender})
def logoutpage(request):
    logout(request)
    return redirect('login')



