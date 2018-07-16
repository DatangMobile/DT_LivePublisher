from django.http import HttpResponse


def PrintHello(e):
    return HttpResponse('Hello world!')