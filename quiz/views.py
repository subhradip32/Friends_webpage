from tracemalloc import start
from django.shortcuts import render
from .models import Entries
from django.http import HttpResponseRedirect 

# Create your views here.
def main(request):
    if request.method == "POST":
        print("method post")
        fav_sub = request.POST.get("fav_sub")
        love_to_do = request.POST.get("love_td")
        fav_colour = request.POST.get("fav_colour")
        fav_game = request.POST.get("fav_game")
        username = request.POST.get("username")
        flag = False
        print(fav_game,fav_colour,fav_sub,username,love_to_do)
        #checking user exist or not 
        data_bs = Entries.objects.all()
        for user in data_bs:
            if user.Username == username:
                flag = True
            else:
                flag = False
        
        if flag:
            #now if user exist in our current entries
            pass
        else:
            #saving the data as a new entry 
            new = Entries()
            new.User = username
            new.fav_subject = fav_sub
            new.fav_colour = fav_colour
            new.love_to_do = love_to_do
            new.fav_game = fav_game
            new.save()
            

    if request.method == "GET":
        username = request.GET.get('username')
    if username==None:
        return HttpResponseRedirect("/authentication")
    # file = open('Questions.txt')
    # data = file.readlines()
    return render(request,"quiz/main.html",{"username":username})