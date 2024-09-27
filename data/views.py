from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo
from rest_framework.generics import CreateAPIView
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer

def mainpage_r(request):
    try :
        user = request.user
        todoThings = Todo.objects.filter(user=user)

    except :
        todoThings = [{'name': "Sign Up/In :)"}]

    print(todoThings)
    return render(request, 'index.html', {"todoThings": todoThings})

def signup(request):
    print(1)
    if request.method == 'POST':
        print(2)
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            auth.login(request, user)
            print('1')
            return redirect('home')  
        except Exception as e:
            print(e)
            messages.error(request, str(e))
            return redirect('home')
    
    else :
        return redirect('home')

def signin(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password']) 
        print(user)
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else :
            return HttpResponse('Error; authenticate, \nyour password or username is wrong.')
    else :
        return redirect('/')

class submit_api(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can create tasks
