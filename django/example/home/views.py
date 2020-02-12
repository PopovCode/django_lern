from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from datetime import datetime
# Create your views here.

# def index_full(request):
#     current_time = datetime.now()
#     context = {
#         'current_time': current_time,
#     }
#     template = loader.get_template('home/index.html')
#     text = template.render(context, request)
#     return HttpResponse(text)

def index(request):

    return render(request, 'generic.html', locals())

