from django.shortcuts import render
from .models import Quote

def main(request):

    quotes = Quote.objects.all()

    return render(request, "quotes/index.html", {"quotes": quotes})