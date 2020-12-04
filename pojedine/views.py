from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><body>Bok, ovo pojedina pocetna strana.<body><html>')
        return render(request, 'pojedine/index.html')

class StrujaView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><body>Bok, ovo pojedina pocetna strana.<body><html>')
        return render(request, 'pojedine/struja.html')

class PlinView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><body>Bok, ovo pojedina pocetna strana.<body><html>')
        return render(request, 'pojedine/plin.html')

class VodaView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><body>Bok, ovo pojedina pocetna strana.<body><html>')
        return render(request, 'pojedine/voda.html')

