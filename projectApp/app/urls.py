from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path('', views.index)
    path('', views.home_view),
    path('admin/', admin.site.urls),
]
