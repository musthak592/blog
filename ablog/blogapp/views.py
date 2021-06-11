from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.


class homeview(ListView):
    model = post
    template_name = 'home.html'

class detailview(DetailView):
    model = post
    template_name = 'article_details.html'

class form(CreateView):
    model = post
    template_name = 'add_post.html'
    fields = '__all__'
class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
class edit(UpdateView):
    model = post
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('home')