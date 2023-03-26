from django.shortcuts import render, HttpResponse


def index(requests):
    return HttpResponse('<h1> hello world </h1>')