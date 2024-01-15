from django.shortcuts import redirect, render
from .forms import SearchForm
from .views import show_entry
from . import util

import re


class SearchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data["entry"]
                entries: list[str] = util.list_entries()

                matches: list[str] = [entry for entry in entries if re.search(
                    query, entry, re.IGNORECASE)]
                

                if query in entries:
                    return redirect('entry', entry=query)
                elif not matches:
                    return redirect('notfound', entry=query)
                else:
                    request.session['matches'] = matches
                    return redirect('matches')
                
        response = self.get_response(request)
        return response
