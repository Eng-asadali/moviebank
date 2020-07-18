from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Movies

# Create your views here.
def movieListView(request):
    return HttpResponse(status=200)

class netflixListView(ListView):
    model = Movies
    template_name = "movies/index.html"
class netflixDetailView(DetailView):
    model= Movies
    template_name = "movies/indexDetailView.html"