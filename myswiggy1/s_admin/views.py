from django.shortcuts import render,redirect
from django.contrib import messages
from s_admin.models import *
from s_admin.forms import *


def s_adminlogin(request):
    return render(request,'sadmin/login.html')


def logincheck(request):
    s_username=request.POST.get('sa1')
    s_password=request.POST.get('sa2')
    try:
        Adminlogin.objects.get(username=s_username, password=s_password)
        request.session['status'] = True
        return render(request, 'Sadmin/adminhome.html')
    except Adminlogin.DoesNotExist:
        messages.error(request,"invalid details")
        return redirect('login')


def adminhome(request):
    return render(request,'Sadmin/adminhome.html')


def adminlogout(request):
    request.session['status']=False
    return redirect('login')


def open_state(request):
    request.session['status'] = True
    try:
        st=StateModel.objects.all()
        return render(request,"Sadmin/open.html",{"sf":StateForm(),"st":st})
    except StateModel.DoesNotExist:
        messages.error(request,"details is empty")
        return render(request,"Sadmin/open.html")


def save_state(request):
    sf=StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        messages.error(request,'state is not saved')
        return render(request,'Sadmin/open.html',{"error":sf})


def state_update(request):
    s_up=request.GET.get('up')
    state=StateModel.objects.get(state_name=s_up)
    return render(request,'Sadmin/update.html',{"state":state,"all":StateModel.objects.all()})


def update_state(request):
    s1=request.POST.get('s1')
    s2=request.POST.get('s2')
    StateModel.objects.filter(state_no=s1).update(state_name=s2)
    return redirect('open_state')


def state_delete(request):
    s_up = request.GET.get('up')
    state = StateModel.objects.get(state_name=s_up).delete()
    return redirect('open_state')


def open_city(request):
    return render(request,'Sadmin/cityopen.html',{"city":CityForm(),"all":CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        messages.error(request, 'state is not saved')
        return render(request, 'Sadmin/cityopen.html', {"error": sf})


def city_update(request):
    s_up = request.GET.get('up')
    city = CityModel.objects.get(city_name=s_up)
    return render(request, 'Sadmin/cityupdate.html', {"city": city, "all": CityModel.objects.all()})


def update_city(request):
    s1 = request.POST.get('s1')
    s2 = request.POST.get('s2')
    s3 = request.POST.get('s3')

    CityModel.objects.filter(city_no=s1).update(city_name=s2,state=s3)
    return redirect('open_state')


def city_delete(request):
    c_up = request.GET.get('up')
    city = CityModel.objects.get(city_name=c_up).delete()
    return redirect('open_city')


def open_area(request):
    return render(request,'Sadmin/areaopen.html',{"area":AreaForm(),"all":AreaModel.objects.all()})


def area_city(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        messages.error(request, 'area is not saved')
        return render(request, 'Sadmin/areaopen.html', {"error": sf})


def area_update(request):
    s_up = request.GET.get('up')
    area = AreaModel.objects.get(area_name=s_up)
    return render(request, 'Sadmin/areaupdate.html', {"area": area, "all": AreaModel.objects.all()})


def update_area(request):
    s1 = request.POST.get('s1')
    s2 = request.POST.get('s2')
    s3 = request.POST.get('s3')

    AreaModel.objects.filter(area_no=s1).update(area_name=s2,area=s3)
    return redirect('open_area')


def area_delete(request):
    c_up = request.GET.get('up')
    area = AreaModel.objects.get(area_name=c_up).delete()
    return redirect('open_area')
