from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Tag
from django.db.models import Count


def main(request):

    quotes_list = Quote.objects.all()

    paginator = Paginator(quotes_list, 5)
    page_number = request.GET.get("page")
    quotes = paginator.get_page(page_number)

    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]

    return render(
        request,
        "quotes/index.html",
        {
            "quotes": quotes,
            "top_tags": top_tags
        }
    )


def tag_search(request, tag_name):

    quotes = Quote.objects.filter(tag__tag=tag_name)

    return render(
        request,
        "quotes/tag.html",
        {"quotes": quotes, "tag": tag_name},
    )


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")

    else:
        form = UserCreationForm()

    return render(request, "quotes/register.html", {"form": form})


@login_required
def add_author(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        born_date = request.POST["born_date"]
        born_location = request.POST["born_location"]
        description = request.POST["description"]

        Author.objects.create(
            fullname = fullname,
            born_date = born_date,
            born_location = born_location,
            description = description
        )
        return redirect("main")
    return render(request, "quotes/add_author.html")


@login_required
def add_quote(request):

    if request.method == "POST":

        text = request.POST.get("text")
        author_id = request.POST.get("author")

        author = Author.objects.get(id=author_id)

        quote = Quote.objects.create(
            text=text,
            author=author
        )

        return redirect("/")

    authors = Author.objects.all()

    return render(
        request,
        "quotes/add_quote.html",
        {"authors": authors}
    )

