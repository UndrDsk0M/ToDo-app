from django.shortcuts import render
from .models import Todo
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

def mainpage_r(request):
    try :
        user = request.user
        todoThings = Todo.objects.filter(user)

    except :
        todoThings = [{'name': "Signup/in to Site :)"}]

    print(todoThings)
    return render(request, 'index.html', {"todoThings": todoThings})

class submit_api(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save(name=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # پاسخ موفقیت‌آمیز
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # پاسخ خطا