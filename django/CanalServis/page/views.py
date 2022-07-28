from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.
def index(request):
    """Index View
    """
    data = Order.objects.all()
    total = sum([d.dollar for d in data])
    template = loader.get_template('pages/index.html')
    context = {
        'total': total,
        'data' : data,
    }
    return HttpResponse(template.render(context, request))