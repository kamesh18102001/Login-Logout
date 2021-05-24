from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class infoForm(forms.Form):
    g=(('MALE','MALE'),('FEMALE','FEMALE'))
    name=forms.CharField(label='Name',max_length=30,help_text='Name')
    gender=forms.CharField(label='Gender',max_length=6,help_text='Gender')
    dob=forms.CharField(label='YYYY-MM-DD')
    branch=forms.CharField(label='Branch',max_length=30)
    phone=forms.CharField(label='Contact Number',max_length=10)
    email=forms.EmailField(label='Email Id',max_length=50)


class registerit(UserCreationForm):
    email=forms.EmailField()
    nickname=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=['username','nickname','email','password1','password2']
