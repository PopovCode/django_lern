from django.shortcuts import render
from .models import tovar
# Create your views here.


def index(request):
    all_tovars = tovar.objects.all()
    return(render(request, 'tovar/index.html', locals()))