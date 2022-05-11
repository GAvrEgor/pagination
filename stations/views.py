from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open("data-398-2018-08-30.csv", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        content = []
        for row in reader:
            content.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_num)
    data = page.object_list
    # name = paginator.get
    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
