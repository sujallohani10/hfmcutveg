import re

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from statistics import mean
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'home.html')

def carrotAndCelery(request):

    url = 'calculateMultipleItems'
    badge_name = 'Carrot & Celery 350G (2080)'
    carrotceleryStr = '{"Carrot":190, "Celery":160}' 
    template_view =  'common.html'

    return render(request, template_view, {'urlName': url, 'badge_name': badge_name, 'itemStr': carrotceleryStr})

def carrotBattons(request):

    url = 'calculateMultipleItems'
    badge_name = 'Carrot Battons 200G (2092)'
    carrotStr = '{"Carrot":205}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': carrotStr})

def carrotCurls(request):

    url = 'calculateMultipleItems'
    badge_name = 'Carrot Curls 400G (9566)'
    curlsStr = '{"Carrot":405}' # The weight should be retrieved from Constant file for no need to change code
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': curlsStr})

def dicedPumpkin(request):

    url = 'calculateMultipleItems'
    badge_name = 'Diced Pumpkin 500G (2046)'
    pumpkinStr = '{"Pumpkin":505}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': pumpkinStr})

def zucchini(request):

    url = 'calculateMultipleItems'
    badge_name = 'Zucchini Zoodles 400G (8968)'
    zucchiniStr = '{"Zucchini":405}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': zucchiniStr})

def beetroot(request):

    url = 'calculateMultipleItems'
    badge_name = 'Beetroot Noodles 400G (4010)'
    beetrootStr = '{"Beetroot":405}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': zucchiniStr})

def cauliflowerRice(request):

    url = 'calculateMultipleItems'
    badge_name = 'Cauliflower Rice 350G (7095)'
    cauliflowerStr = '{"Cauliflower":355}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': cauliflowerStr})

def shreddedKale(request):

    url = 'calculateMultipleItems'
    badge_name = 'Shredded Kale 150G (2098)'
    kaleStr = '{"Kale":155}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': kaleStr})

def mixCapsicum(request):

    url = 'calculateMultipleItems'
    badge_name = 'Mix Capsicum Trio 300G (2083)'
    capsicumStr = '{"Green Capsicum":100, "Yellow Capsicum":100, "Red Capsicum":100}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr':capsicumStr})

def calculateMultipleItems(request):
    # validating...i.e. request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

         # data from ajax
        unit = request.POST.get('unit') #unit is the total order of item
        itemStr = request.POST.get('itemStr')
        item_dict = json.loads(itemStr)
        print(type(item_dict))
        print(item_dict)

        displayMessage = ""

        for item, itemNetWeight in item_dict.items():
            itemWeight = int(unit) * int(itemNetWeight) / 1000 #converting to kilo gram

            displayMessage += str(item) + " weight in KG: " + str(itemWeight) + "\n<br>"

        responseList = []
        responseList.append(displayMessage);

        return JsonResponse({"responseList": responseList}, status=200)

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