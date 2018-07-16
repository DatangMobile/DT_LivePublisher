import datetime
from django.http import HttpResponse
from django.shortcuts import render

def PrintCurrentTime(e):
    Now = datetime.datetime.now()
    TempString = "Now Time is %s" % Now
    context = {}
    context['order_time'] = TempString
    return render(e, 'index.html', context)