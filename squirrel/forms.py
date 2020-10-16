from django.forms import ModelForm
from .models import SquirrelDetail
class Form(ModelForm):
    class Meta:
        model = SquirrelDetail
        fields = '__all__'
