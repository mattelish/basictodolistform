from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from django.views import generic
from django.utils import timezone
from todolist.models import Todo
from .models import Todo
from todolist.forms import TodoForm
from django.views.generic.edit import FormView
from django.forms import ModelForm

# Create your views here.


def index(request):
    if request.method == 'POST':
       form = TodoForm(request.POST)
       if form.is_valid():
          form.save()
          
          return HttpResponseRedirect('/todolist/')
    else:
        form = TodoForm()
    
    return render( request, 'new_index.html', { 'form': form})
