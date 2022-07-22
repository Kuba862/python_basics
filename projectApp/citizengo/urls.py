from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('petition/<str:id>/', views.petitionPage, name="petition"),
    path('about-us/', views.aboutUsPage, name="about-us"),
    path('victories/', views.victoriesPage, name="victories"),
]
