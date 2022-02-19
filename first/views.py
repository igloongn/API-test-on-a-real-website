from django.http import JsonResponse
from django.shortcuts import render
import requests as req
import json

# Create your views here.
def index(request):
    p={}
    p['word']='This is Very Good'
    return render(request, 'index.html', p)
    

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
    res=req.get(url)
    json_res=res.json()
    # print(json_res)

    data=res.content
    # This is to Copy the API JSON Contents to a file
    with open('data.json', 'w') as outfile:
        json.dump(json_res['articles'], outfile)

    p['news']=json_res['articles']
    return render(request, 'news.html', p)
    # return JsonResponse(res.content, safe=False)
    

