import re

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from statistics import mean
from django.http import JsonResponse


def index(request):
    return render(request, 'home.html')

def carrotAndCelery(request):
    return render(request, 'calculator.html')


def validate_amount(request):
    amount = request.POST.get('amount')
    data = {}
    if not re.match(r'^[1-9]\d*(\.\d{1,2})?$', amount) or amount == '':
        data["type"] = 'error'
        data["message"] = 'Amount should be non-negative and upto two decimal point'
    return JsonResponse(data)


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
