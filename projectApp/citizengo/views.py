from django.shortcuts import render
from .models import Petition, Creator
from django.utils.translation import gettext as _

def homePage(request):
    petitions = Petition.objects.all()[:6]
    context = {
        'petitions': petitions,
    }
    return render(request, 'citizengo/homePage.html', context)

def petitionPage(request, id):
    petition = Petition.objects.get(id=id)
    context = {
        "petition": petition,
    }
    return render(request, 'citizengo/petitionPage.html', context)

def aboutUsPage(request):
    return render(request, 'citizengo/aboutUs.html')

def victoriesPage(request):
    return render(request, 'citizengo/victories.html')  

def creator(request):
    authors = Creator.objcts.all()
    context = {
        "author": authors
    }
    return render(request, 'citizengo/homePage.html', context)

def victoriesPage(request):
    petitions = Petition.objects.all()
    context = {
        "petitions": petitions,
    }  
    return render(request, 'citizengo/victories.html', context)


