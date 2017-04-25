#views.py
from django.http import HttpResponse

def hello(request):
	return HttpResponse("My new web view")
