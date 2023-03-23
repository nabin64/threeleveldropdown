from django.shortcuts import render, redirect

from app.models import *

def home(request):
    province = Province.objects.all()
    context = {
        "province":province
    }
    return render(request,'add_district.html',context)


def LOAD_DISTRICT(request):
    province_id = request.GET.get('provinceid')
    district = District.objects.filter(province_id = province_id).all()
    context = {
        "district":district
    }
    return render(request,'district_drop_down.html',context)


def LOAD_LOCAL(request):
    district_id = request.GET.get('districtid')
    local = Local.objects.filter(district_id = district_id ).all()
    context = {
        "local":local
    }
    return render (request, 'local_level_drop_down.html',context)

def ADD_PROJECT(request):
    if request.method =="POST":
        province_id = request.POST.get('province')
        district_id = request.POST.get('district')
        local_id  = request.POST.get('local')
        project = request.POST.get('project')
        province = Province.objects.get(id=province_id)
        district = District.objects.get(id=district_id)
        local = Local.objects.get(id = local_id)
        

   
    
        project = Project(
            name = project,
            local = local,
            district = district,
            province = province,
        )
        project.save()
        return redirect('home')
