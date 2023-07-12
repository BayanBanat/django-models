from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack


class SnackDetailView(DeleteView):
    template_name = 'snack_detail.html'
    model = Snack