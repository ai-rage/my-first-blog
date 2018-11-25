from django.shortcuts import render
from django.http import HttpResponse

def posts(requsts):
    return HttpResponse("Привет. Этот текст получен из Представления posts.")