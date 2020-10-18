from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['name', 'email', 'password']
         
    widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput( render_value = True , attrs={'class':'form-control'}), #render_value = True --> 'edit' button/home/dipendra/DB_Workshop/BES click password value pani tyo password field ma dekhauna ko lagi yo 'render_value' use huncha.
        }      
