import re
import random as r

from django.shortcuts import redirect, render
from encyclopedia.forms import SearchForm
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': SearchForm()
    })


def show_entry(request, entry: str):
    return render(request, "encyclopedia/entry.html", {
        'entry': entry,
        'content': util.convert_md(entry),
        'form': SearchForm()
    })


def notfound(request, entry):
    return render(request, "encyclopedia/notfound.html", {
        'entry': entry,
        'form': SearchForm()
    })


def matches(request):
    matches = request.session.get('matches', [])
    return render(request, "encyclopedia/matches.html", {
        'matches': matches,
        'form': SearchForm(),
    })


def random_entry(request):
    entries = util.list_entries()
    entry = entries[r.randint(0, len(entries) - 1)]

    return redirect('entry', entry=entry)


def create_page(request):
    return render(request, "encyclopedia/not_implemented.html", {
        'form': SearchForm(),
    })


def edit_page(request):
    return render(request, "encyclopedia/not_implemented.html", {
        'form': SearchForm(),
    })
