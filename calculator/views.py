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

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr': beetrootStr})

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

def stirFry(request):

    url = 'calculateMultipleItems'
    badge_name = 'Stir Fry Veg Broc/Caul 450G (20801)'
    stirfryStr = '{"Cauliflower":100, "Brocoli":65, "Carrot":67, "Snow Peas":50, "Mushroom":50, "Red Capsicum":16, "Yellow Capsicum":40}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr':stirfryStr})

def asianMix(request):

    url = 'calculateMultipleItems'
    badge_name = 'Asian Mix 400G (2104)'
    asianStr = '{"Coleslaw":150, "Snow Peas":50, "Mushroom":28, "Red Capsicum":50}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr':asianStr})

def coleslaw(request):

    url = 'calculateMultipleItems'
    badge_name = 'Coleslaw W/SP Onion 240G (2097)'
    coleslawStr = '{"Coleslaw":245}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr':coleslawStr})

def entertainmentPack(request):

    url = 'calculateMultipleItems'
    badge_name = 'Entertainment Pack 280G (2100)'
    entertainmentStr = '{"Carrot":100, "Celery":100}'
    template_view =  'common.html'

    return render(request, template_view, {'urlName':url, 'badge_name':badge_name, 'itemStr':entertainmentStr})

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