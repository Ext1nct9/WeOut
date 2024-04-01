from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



def main(request):
    return HttpResponse('<h1>Hello World,</h1> <h2>from Django</h2>')


