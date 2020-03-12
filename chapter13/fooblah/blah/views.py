from django.shortcuts import render
from django.template import Template, Context


# Create your views here.
import datetime
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("My new web view")


def my_date(request):
    now = datetime.datetime.now()
    html = "<html><body>The current time is %s.</body></html>" % now
    return HttpResponse(html)


def template_my_date(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ tempdate }}.</body></html>")
    html = t.render(Context({'tempdate': now}))
    return HttpResponse(html)


def d2(request):
    calc = 2*2
    now = datetime.datetime.now()
    my_dict = {'thedate': now, 'mcalc': calc}
    return render(None, "date2.html", my_dict)
