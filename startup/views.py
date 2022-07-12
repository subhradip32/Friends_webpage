
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Authentication

# Create your views here.
def Start(request):
    if request.method == "POST":
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        data_db = Authentication.objects.all()
        user_exist = False
        log_pas = ""
        #manipulating the user datas 
        for users in data_db:
            if users.Username == Username:
                user_exist = True
                log_pas = users.Password
            else:
                user_exist = False
        #checking login details here
        if "login_bt" in request.POST:
            print("Login")

            if user_exist:
                if Password == log_pas:
                    url = "/quiz/?username={}".format(Username)
                    return HttpResponseRedirect(url) #taking the name of the url
        #creating new registrations    
        elif "register_bt" in request.POST:
            print("register")
            
            if user_exist:
                return render(request,'startup/main.html',{
                    "error":"Username already exists"
                })
            else:
                obj = Authentication()
                obj.Username = Username
                obj.Passwrod = Password
                obj.save()
    #by default render             
    return render(request,'startup/main.html')