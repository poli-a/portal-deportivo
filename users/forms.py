from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.forms import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')
 
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'imagen')