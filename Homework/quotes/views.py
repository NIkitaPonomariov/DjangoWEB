from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote


def main(request):

    quotes_list = Quote.objects.all()

    paginator = Paginator(quotes_list, 5)   # 5 quotes per page

    page_number = request.GET.get("page")

    quotes = paginator.get_page(page_number)

    return render(request, "quotes/index.html", {"quotes": quotes})