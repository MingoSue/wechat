from django import forms
from .models import User, Code

class UserForm(forms.ModelForm):
    class Meta:
        model = User

class CodeInfo(forms.ModelForm):
    class Meta:
        model = Code
