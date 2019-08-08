from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ParsingDB
from .forms import InputForm
from django.views.generic import View
from .pars import pars, parsMore

# Create your views here.

class Parsing(View):
    def get(self, request):
        form = InputForm()
        return render(request, 'drom_pars/main_page.html', context={'form': form})

    def post(self, request):
        inputForm = InputForm(request.POST)
        href = ParsingDB.objects.filter(href__iexact=request.POST['href'])

        if len(href) == 0:
            new_item = ParsingDB(href=request.POST['href'])
            new_item.save()

        id = ParsingDB.objects.get(href__iexact=request.POST['href'])
        otvet = pars(request.POST['href'])

        return render(request, 'drom_pars/main_page.html', context={'form': inputForm, 'hrefs': otvet, 'item': id})

class ParsMore(View):
    def get(self, request, id):
        item = get_object_or_404(ParsingDB, id__iexact=id)
        items = parsMore(item.href)
        return render(request, 'drom_pars/info.html', context={'items': items})



