"""kipia URL Configuration

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
from django.urls import path
from .views import *

urlpatterns = [
    path('', ValvesView.as_view(), name='valves_node_list'),
    path('add/', ValveAdd.as_view(), name='valve_node_add'),
    path('<str:slug>/', ValveDetail.as_view(), name='valve_detail'),
    path('<str:slug>/update/', ValveUpdate.as_view(), name='valve_update'),
    path('<str:slug>/delete/', ValveDelete.as_view(), name='valve_delete'),

]
