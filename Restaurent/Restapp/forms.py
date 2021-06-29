from django.forms import ModelForm
from Restapp.models import Restaurent

class ReForm(ModelForm):
	class Meta:
		model = Restaurent;
		fields = "__all__"