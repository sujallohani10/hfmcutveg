import re

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from statistics import mean
from django.http import JsonResponse


def index(request):
    return render(request, 'home.html')

def carrotAndCelery(request):
    return render(request, 'calculator.html', {'urlName':'calculateCarrrotCelery','badge_name':'Carrot & Celery 350G (2080)'})


def carrotBattons(request):
    return render(request, 'calculator.html', {'urlName':'calculateCarrotBattons','badge_name':'Carrot Battons 200G (2092)'})

def carrotCurls(request):
    return render(request, 'calculator.html', {'urlName':'calculateCarrotCurls','badge_name':'Carrot Curls 400G (9566)'})


def calculateCarrrotCelery(request):
    # validating...i.e. request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

        # data from ajax
        unit = request.POST.get('unit')
        print(unit)

        # carrot quantity in 350G: 190G
        carrot = int(unit) * 190 / 1000 #Python follows PEMDAS (Parentheses Exponentiation Multiplication Division Addition Subtraction) for math calculation
        carrot = round(carrot, 2) 
        print(carrot)      

        # Celery quantity in 350G: 160G
        celery = int(unit) * 160 / 1000 
        celery = round(celery, 2)
        print(celery) 

        responseList = []
        responseList.append("Carrot weight in Kg: " + str(carrot) + "\n<br>"+
                            "Celery weight in Kg: " + str(celery)
        );

        return JsonResponse({"responseList": responseList}, status=200)

def calculateCarrotBattons(request):
    # validating...i.e. request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

        # data from ajax
        unit = request.POST.get('unit') #unit is the total order of item
        print(unit)

        # carrot quantity in 200G
        carrot = int(unit) * 200 / 1000 #Python follows PEMDAS (Parentheses Exponentiation Multiplication Division Addition Subtraction) for math calculation
        carrot = round(carrot, 2) 
        print(carrot)

        responseList = []
        responseList.append("Carrot weight in Kg: " + str(carrot) + "\n<br>"
        );

        return JsonResponse({"responseList": responseList}, status=200)


def calculateCarrotCurls(request):
    # validating...i.e. request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

        # data from ajax
        unit = request.POST.get('unit') #unit is the total order of item
        print(unit)

        # carrot quantity in 400G
        carrot = int(unit) * 400 / 1000
        carrot = round(carrot, 2) 
        print(carrot)

        responseList = []
        responseList.append("Carrot weight in Kg: " + str(carrot) + "\n<br>"
        );

        return JsonResponse({"responseList": responseList}, status=200)