from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)

def welcome(request):
    if request.user.is_authenticated:
        logger.debug("success actual")
        print (__name__)
        return render(request, 'home/home.html')
    else:
        return HttpResponseRedirect('/login')