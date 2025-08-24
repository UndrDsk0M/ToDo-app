from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.core.cache import cache
from django.contrib import auth
from .models import Todo
from captchaSaz import *
import time
import json
import os

# run the scheduler in background
scheduler = BackgroundScheduler()
scheduler.start()

def delete_captcha_path(path):
    os.remove(path)

def mainpage_r(request):
    todoThings = None
    if request.user.is_authenticated:
        user = request.user
        todoThings = Todo.objects.filter(user=user)[::-1]
        print(list(todoThings))
    return render(request, 'index.html', {"todoThings": list(todoThings)})

def signup(request):
    if request.method == 'POST':
        captcha_id = request.POST.get('uniqe')
        captcha_usr = request.POST.get('captcha')
        
        captcha = cache.get(captcha_id)
        if check(captcha[0], captcha_usr):
            delete_captcha_path(captcha[1])
            cache.delete(captcha_id)
        else :
            return HttpResponse("Wrong captcha try again")
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                auth.login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Incorrect password")
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            auth.login(request, user)
            return redirect('home')

def signin(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], 
                                password=request.POST['password']) 
        if user is not None :
            auth.login(request, user)
            return redirect('home')
        else :
            return HttpResponse('Error; authenticate, \nyour password or username is wrong.')
    else :
        return redirect('home')


class submit(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            body = request.data.get("task")
            Todo.objects.create(user=request.user, name=body)

        return Response({"status": 200})

class checked(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            body = request.data.get("task")
            print(body, request.user)
            taskObject = Todo.objects.get(id=body, user=request.user)
            print(taskObject)
            taskObject.delete()

        return Response({"status": 200})
    
class captcha(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            captcha_img, captcha_txt = generate(text=randomText(length=5, uppercase_char=False, lowercase_char=False, number=True))
            tt = str(time.time()).replace('.', '')
            uniqe = request.data.get("uniqe")
            captcha_path = f"./static/captcha_imgs/captcha-{tt}.jpg"
            cache.set(uniqe, [captcha_txt, captcha_path], timeout=300)
            captcha_img.save(captcha_path)
            
            global scheduler 
            run_time = datetime.now() + timedelta(seconds=315)
            scheduler.add_job(delete_captcha_path, 'date', run_date=run_time, args=[captcha_path])
            
            
            return Response({"status": 202, "captcha_url": f"captcha-{tt}.jpg"})
        return Response({"status": 403})
    
class Subtask(APIView):
    def post(self, request):
        print("of")