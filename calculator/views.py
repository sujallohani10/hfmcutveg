import re

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from statistics import mean
from django.http import JsonResponse


def index(request):
    return render(request, 'calculator.html')


def validate_amount(request):
    amount = request.POST.get('amount')
    data = {}
    if not re.match(r'^[1-9]\d*(\.\d{1,2})?$', amount) or amount == '':
        data["type"] = 'error'
        data["message"] = 'Amount should be non-negative and upto two decimal point'
    return JsonResponse(data)


def calculateGrocery(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":

        # Task to do
        # GUI make similar to ATO tax calculator

        # data from ajax
        nameList = request.POST.getlist('name[]')
        amountList = request.POST.getlist('amount[]')
        amountList = list(map(float, amountList))

        # conversion of lists to dictionary
        # using zip()
        nameAmountDict = dict(zip(nameList, amountList))
        print("Resultant dictionary is : " + str(nameAmountDict))

        average = mean(amountList)
        average = round(average, 2)
        averageText = "<b>Note</b>: Each user subjected to pay: $"+str(average)
        print("The average is ", average)
        print(nameAmountDict)

        responseList = []
        for name, value in nameAmountDict.items():
            remainder = round(value - average, 2)  # 50 is average value
            if remainder == 0:
                responseList.append("Neither pay nor receive: " + name)
            elif remainder > 0:
                responseList.append(name + " Receive: $" + str(abs(remainder)))
            else:
                responseList.append(name + " Pay: $" + str(abs(remainder)))

        return JsonResponse({"responseList": responseList, "averageText": averageText}, status=200)
