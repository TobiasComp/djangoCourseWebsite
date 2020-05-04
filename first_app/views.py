from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from first_app.models import User1
from . import forms
from first_app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken

# Create your views here.

def index(request):
    return HttpResponse("<em>Helllo!!</em>")

def users(request):
    allUsers = User1.objects.all()
    user_dict = {'Users': allUsers}
    return render(request, 'first_app/users.html', user_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data['name'])

    return render(request, 'first_app/form_page.html', {'form': form})

def add_user_view(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("There was an error in the add user form")
    return render(request, 'first_app/add_user.html', {'form': form})

def login(request):
    form = loginForm()
    message = ""
    data = {'message': message, 'form': form}

    if request.method == 'POST':
        print(request.POST)
        my_first_name = dict(request.POST)['first_name'][0]
        password = dict(request.POST)['password'][0]
        print(my_first_name)
        user = User1.objects.filter(first_name = my_first_name)
        # print("This is the user", " ", user[0].password)

        if User1.objects.filter(first_name = my_first_name):
            print("there is such a user")
            if list(User1.objects.filter(first_name = my_first_name))[0].password == password:
               print("youre in")
               return render(request, 'first_app/users.html')
            else:
                print("wrong password")
                message = "wrong password"
                data = {'message':message,'form':form}
                return render(request, 'first_app/login.html', data)
        else:
            print("there is no such user!!")
            message = "there is no such user"
            data = {'message': message, 'form': form}
            return render(request, 'first_app/login.html', data)
    return render(request, 'first_app/login.html', data)

# def userJson(request):
#     users = User1.objects.values()
#     print(users)
#     return JsonResponse(list(users), safe=False)

#ADDED FOR AUTH
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
