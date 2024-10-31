from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

#def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })