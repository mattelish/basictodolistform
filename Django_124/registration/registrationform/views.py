from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from django.views import generic
from django.utils import timezone
from registrationform.models import Register
from .models import Register
from registrationform.forms import RegisterForm
from django.views.generic.edit import FormView
from django.forms import ModelForm
#from address.forms import AddressField
# Create your views here.


def index(request):
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
          #form = form.save(commit=false)
          form.save()
          
          return HttpResponseRedirect('/registrationform/')
    else:
        form = RegisterForm()
    
    return render( request, 'registrationform/register.html', { 'form': form})
    