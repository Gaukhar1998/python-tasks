from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model, authenticate

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    email = forms.EmailField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter email'}))
    username = forms.CharField(widget=forms.TextInput
            (attrs={'placeholder': 'Enter username'}))
    class Meta:
        model = User
        fields = ['username','email','password']


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise  forms.ValidationError("This user doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args,**kwargs)