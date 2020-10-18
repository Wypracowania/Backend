from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=20)
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Password'}), max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=20)
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Password'}), max_length=20)
