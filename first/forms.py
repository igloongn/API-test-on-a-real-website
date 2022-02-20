from django import forms
from .models import UserModel
#DataFlair
class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'