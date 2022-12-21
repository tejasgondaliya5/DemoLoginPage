from xml.dom import UserDataHandler
from django.shortcuts import redirect, render
from .forms import InputForm
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
import hashlib
from django.db.models import Q
from .ResponsFile import *
from .allFunction import *
import requests
import json
from django.contrib import messages

# Create your views here.

def call_login_API(userName, password):
    url = f"{BASE_DOMAIN}/login_api"

    payload = json.dumps({
    "userName": userName,
    "password": password
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)
    return response



def login(request):
    if request.method=="POST":
        form=InputForm(request.POST)
        if form.is_valid():
            response = call_login_API(request.POST['userName'], request.POST['password'])
            if response['status']=="Success":
                return redirect('home')
            else:
                messages.add_message(request,messages.ERROR,response["message"])
        else:
            messages.add_message(request,messages.ERROR,'Invalid Captch Code.')
    form=InputForm()
    return render(request, 'login.html', {'form':form})

def home(request):
    return render(request, 'home.html')

@api_view(['POST'])
def login_api(request):
    if request.data:
        try:
            UserData = User.objects.get(Q(userName=request.data['userName']) | Q(email=request.data['userName']), isDeleted="0")
            if UserData.password ==request.data['password']:
                serializer = UserSerializer(UserData)
                return Response(getResponseByType("Success", "Login success.", "Login API", "Login API", "Userdata", serializer.data))
            return Response(getResponseByType("Fail", "Invalid Password.", "Create Signin API", "Create Signin API", "Value", f"Invalid Password."))
        except Exception as e:
            return Response(getResponseByType("Fail", "Invalid UserName.", "Create Signin API", "Create Signin API", "Value", f"Invalid UserName."))
    return Response(getResponseByType("Fail", "insert valid data is reqired, please try again.", "Create add or update Department API", "Create add or update Department API", "Value", "insert valid data is reqired, please try again."))





