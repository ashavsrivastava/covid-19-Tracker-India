from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"India"}

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8af0639d48msh8a82bb6d4dde01fp13019fjsn225c99a3094c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']
    d=data[0]
    print(d)    

    context ={
        'total' :d['cases']['total'],
        'rec' : d['cases']['recovered'],
        'death' : d['deaths']['total'],
        'newcases' : d['cases']['new'],
        'critical' :d['cases']['critical'],
        'totaltests' : d['tests']['total']
    }

    return render(request,'index.html',context) 