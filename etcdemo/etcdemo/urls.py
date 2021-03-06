"""etcdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import hello
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello.hello, name='hello'),
    path('demo01/', views.demo01, name='similar'),
    path('demo02/', views.demo02, name='dragdrop'),
    path('chart01/', views.chart01, name='chart01'),
    path('chart02/', views.chart02, name='chart01'),
    path('chart03/', views.chart03, name='chart01'),
    path('chart04/', views.chart04, name='chart01'),
    path('chart05/', views.chart05, name='chart01')
]
