from django.shortcuts import render
from .models import Petition, Topics

def homePage(request):
    petitions = Petition.objects.all()
    context = {
        'petitions': petitions,
    }
    return render(request, 'citizengo/homePage.html', context)

def petitionPage(request, id):
    petition = Petition.objects.get(id=id)
    context = {"petition": petition}
    return render(request, 'citizengo/petitionPage.html', context)

def aboutUsPage(request):
    return render(request, 'citizengo/aboutUs.html')

def victoriesPage(request):
    return render(request, 'citizengo/victories.html')    

def topicsList(request):
    topics = Topics.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'citizengo/homePage.html', context)

