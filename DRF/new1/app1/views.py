from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Fun(request):
    emp = {
        'Name' : 'mani',
        'Age' : 20,
        'Country' : 'india'
    }
    new = f"<h2>Name : {emp['Name']}, Age : {emp['Age']}, Country : {emp['Country']}</h2>"
    return HttpResponse(new)

import json
def J_son(request):
    emp = {
        'Name': 'mani',
        'Age': 20,
        'Country': 'india'
    }
    json_dict = json.dumps(emp)
    return HttpResponse(json_dict)


# Another way to JSon formate.
from django.http import JsonResponse
def J_son2(request):
    emp = {
        'Name': 'mani',
        'Age': 20,
        'Country': 'india'
    }

    return JsonResponse(emp)
