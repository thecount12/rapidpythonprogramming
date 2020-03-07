from django import forms
from models import REG

class PostReg(forms.ModelForm):
        class Meta:
                model=REG
                fields=('username','email','password','hint',)


