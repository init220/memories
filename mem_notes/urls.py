"""memories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from mem_notes.views import add_note, note_detail, note_list, policy

urlpatterns = [
    path('add_note/', add_note, name='add_note'),
    path('policy/', policy, name='policy'),
    path('', note_list, name='note_list'),
    path('note_detail/<int:pk>/', note_detail, name='note_detail'),
]
