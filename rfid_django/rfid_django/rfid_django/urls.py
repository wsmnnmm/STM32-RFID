"""rfid_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test", views.test),
    path("getcarid", views.getcarid),
    path("home",views.Homeclass.as_view()),
    path("my_register",views.Registerclass.as_view()),
    path("my_register_post/",views.my_register_post),
    path("my_report",views.Reportclass.as_view()),
    path("my_report_post/",views.my_report_post),
    path("my_record",views.Recordclass.as_view()),
]
