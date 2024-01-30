import random as r

from django.shortcuts import redirect, render, HttpResponse
from encyclopedia.forms import SearchForm
from . import util

def index(request) -> HttpResponse:
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': SearchForm()
    })

def show_entry(request, entry: str) -> HttpResponse:
    return render(request, "encyclopedia/entry.html", {
        'entry': entry,
        'content': util.convert_md(entry),
        'form': SearchForm()
    })


def notfound(request, entry) -> HttpResponse:
    return render(request, "encyclopedia/error.html", {
        'entry': entry,
        'form': SearchForm()
    })


def matches(request) -> HttpResponse:
    matches = request.session.get('matches', [])
    return render(request, "encyclopedia/matches.html", {
        'matches': matches,
        'form': SearchForm(),
    })


def random_entry(request):
    entries = util.list_entries()
    entry = entries[r.randint(0, len(entries) - 1)]

    return redirect('entry', entry=entry)


def create_page(request) -> HttpResponse:
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title):
            return render(request, 'encyclopedia/create.html', {
                'title': title,
                'content': content,
                'exists': True,
                'form': SearchForm()
            })
        util.save_entry(title, content)
        return redirect('entry', entry=title)
    
    return render(request, 'encyclopedia/create.html', {
        'form': SearchForm(),
    })


def edit_page(request, entry):
    content = util.get_entry(entry)
    if request.method == 'POST':
        content = request.POST['content']
        util.save_entry(entry, content)
        return redirect('entry', entry=entry)
    
    return render(request, "encyclopedia/edit.html", {
        'form': SearchForm(),
        'entry': entry,
        'content': content
    })
