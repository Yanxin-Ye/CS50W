from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    now = datetime.now()
    is_newyear = now.month == 1 and now.day == 1
    # return HttpResponse("new year")
    return render(request, "newyear/index.html", {"is_newyear": is_newyear})
