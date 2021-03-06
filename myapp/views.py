import re
from django.http.request import HttpHeaders
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View
from .form import Signupform
from django.http import JsonResponse
from .models import Register

# Create your views here.


def home(request):
    form = Signupform(request.POST, request.FILES)
    res_data = {}
    if request.is_ajax and request.method == "POST":
        if form.is_valid():
            form.save()
            res_data['username'] = form.cleaned_data.get('username')
            res_data['status'] = 'ok'
            return JsonResponse(res_data)

    context = {
        'form': form
    }
    return render(request, 'index.html', context=context)
