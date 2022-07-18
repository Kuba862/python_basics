from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def index(request):
    return HttpResponse("Hello There")

def home_view(request):
    context = {
        "name": "Jakub",
        "lastName": "Rejch",
    }
    form = InputForm(request.POST or None)
    context['form'] = InputForm()
    return render(request, "home.html", context)