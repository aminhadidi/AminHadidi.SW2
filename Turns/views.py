from django.shortcuts import render
from . import models

def Turns_list(request):
    turns = models.Turn.objects.all().order_by('date')
    args = {'Turns':turns}
    return render(request, 'Turns/Turns_list.html',args)

def Turns_list_amin(request):
    turns1 = models.Turn.objects.all().order_by('date')
    args1 = {'Turns_amin':turns1}
    return render(request, 'Turns/Turns_list_amin.html',args1)

def Turns_list_mehrdad(request):
    turns2 = models.Turn.objects.all().order_by('date')
    args2 = {'Turns_mehrdad':turns2}
    return render(request, 'Turns/Turns_list_mehrdad.html',args2)

def Turns_list_navid(request):
    turns3 = models.Turn.objects.all().order_by('date')
    args3 = {'Turns_navid':turns3}
    return render(request, 'Turns/Turns_list_navid.html',args3)

def Turns_list_nima(request):
    turns4 = models.Turn.objects.all().order_by('date')
    args4 = {'Turns_nima':turns4}
    return render(request, 'Turns/Turns_list_nima.html',args4)
