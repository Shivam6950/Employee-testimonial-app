from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()
    
    name="Learning Django"
    list_of_programs=[
        'Program to check even or odd',
        'Program to check prime number',
        'Program to print all prime numbers from 1 to 100',
        'Program to print pascals triangle'
    ]
    student={
        "student_name":"Hammer",
        "student_college":"XYZ",
        "student_city":"Delhi" 
    }
    data={
        "date":date,
        "isActive":isActive,
        "name":name,
        "list_of_programs":list_of_programs,
        "student_data":student
    }


    #return HttpResponse("<h2>Hello this is index page</h2>" + str(date))
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h3>This is about page</h3>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h3>This is services page</h3>")
    return render(request,"services.html",{})

