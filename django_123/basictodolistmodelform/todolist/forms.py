

from models import Todo
from django.forms import ModelForm






# using ModelForm
class TodoForm(ModelForm):
   
	class Meta:
		model = Todo
		fields = '__all__'
		