from models import Register
from django.forms import ModelForm
from address.forms import AddressField

# using ModelForm
class RegisterForm(ModelForm):
   
	class Meta:
		model = Register
		#fields = '__all__'
		fields = ['First_name','Last_name','Sex','Phone_number','Email','Address','pub_date']
		