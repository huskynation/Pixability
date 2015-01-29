from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	uploadedfile = forms.FileField()
	