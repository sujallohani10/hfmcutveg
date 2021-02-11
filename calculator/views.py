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

    url = 'calculateCommonMethod'
    badge_name = 'Carrot Battons 200G (2092)'
    weight = 205
    displayMessage = "Carrot weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def carrotCurls(request):

    url = 'calculateCommonMethod'
    badge_name = 'Carrot Curls 400G (9566)'
    weight = 405
    displayMessage = "Carrot weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def dicedPumpkin(request):

    url = 'calculateCommonMethod'
    badge_name = 'Diced Pumpkin 500G (2046)'
    weight = 505
    displayMessage = "Pumpkin weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def zucchini(request):

    url = 'calculateCommonMethod'
    badge_name = 'Zucchini Zoodles 400G (8968)'
    weight = 405
    displayMessage = "Zucchini weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def beetroot(request):

    url = 'calculateCommonMethod'
    badge_name = 'Beetroot Noodles 400G (4010)'
    weight = 405
    displayMessage = "Beetroot weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def cauliflowerRice(request):

    url = 'calculateCommonMethod'
    badge_name = 'Cauliflower Rice 350G (7095)'
    weight = 355
    displayMessage = "Cauliflower weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def shreddedKale(request):

    url = 'calculateCommonMethod'
    badge_name = 'Shredded Kale 150G (2098)'
    weight = 155
    displayMessage = "Kale weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

def mixCapsicum(request):

    url = 'calculateCommonMethod'
    badge_name = 'Mix Capsicum 300G (2083)'
    weight = 100
    displayMessage = "Green, Yellow & Red Capsicum each weight in Kg: "
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'weight': weight, 'message':displayMessage})

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

def calculateCommonMethod(request):
    # validating...i.e. request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

        # data from ajax
        unit = request.POST.get('unit') #unit is the total order of item
        weight = request.POST.get('weight')
        displayMessage = request.POST.get('message')
        print(unit)

        # calculation
        item = int(unit) * int(weight) / 1000 #converting to kilo gram
        item = round(item, 2) 
        print(item)

        responseList = []
        responseList.append(displayMessage + str(item) + "\n<br>"
        );

        return JsonResponse({"responseList": responseList}, status=200)