from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# from rest_framework import status

# Create your views here.
from django.views import View
from requests import Response

from home.models import Wallet, Category, Spending, DetailSpending


class api(View):
    def get(self, request):
        if request.user.is_authenticated:
            Spen = DetailSpending.objects.select_related('spending')
            a = []
            for i in Spen:
                d = model_to_dict(i)
                d["category"] = model_to_dict(i.category)
                d["spending"] = model_to_dict(i.spending)
                d["wallet"] = model_to_dict(i.wallet)
                a.append(d)
            return JsonResponse(a, safe=False)
        else:
            return render(request, 'home/index.html')


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home/index.html')
        else:
            return render(request, 'home/home.html')
