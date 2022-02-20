from ast import Param
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import requests as req
import json

from .forms import UserModelForm
from .models import UserModel

# Create your views here.
def index(request):
   return redirect(news)
    

def request(request):
    p={}
    api_key='7592c6a9adcf478ab80bd16bacb6e0ac'
    url=f'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api_key}'
    res=req.get(url)
    json_res=res.json()
    # print(json_res)

    data=res.content
    # This is to Copy the API JSON Contents to a file
    with open('data.json', 'w') as outfile:
        json.dump(json_res['articles'], outfile)

    p['news']=json_res['articles']
    # return render(request, 'requests.html', p)
    return JsonResponse(json_res, safe=False)
    
def news(request):
    p={}
    api_key='7592c6a9adcf478ab80bd16bacb6e0ac'
    url=f'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api_key}'
    # url=f'https://newsapi.org/v2/everything?q=apple&from=2022-02-18&to=2022-02-18&sortBy=popularity&apiKey={api_key}'
    res=req.get(url)
    json_res=res.json()
    # print(json_res)

    data=res.content
    # This is to Copy the API JSON Contents to a file
    with open('data.json', 'w') as outfile:
        json.dump(json_res['articles'], outfile)

    p['news']=json_res['articles']

    # p['userForm']=UserModelForm

    return render(request, 'news.html', p)

def create(request):
    params={}
    try:
        user= UserModel.objects.get(firstname=request.POST['firstname'])
        params['status']='exist'
        params['message']='The username you entered has already been taken. Please try another username.'
    except UserModel.DoesNotExist:
        Userdata_upload = UserModelForm(request.POST, request.FILES)
        if Userdata_upload.is_valid():
            Userdata_upload.save()

            params['firstname']=request.POST['firstname']
            params['lastname']=request.POST['lastname']
            params['status']='uploaded'
        else:
            params['status']='failed'
        
    return JsonResponse(params)