from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.homePage, name="home"),
    path('petition/<str:id>/', views.petitionPage, name="petition"),
    path('about-us/', views.aboutUsPage, name="about-us"),
    path('victories/', views.victoriesPage, name="victories"),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
