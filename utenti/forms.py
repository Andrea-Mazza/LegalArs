from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, ResetPasswordKeyForm
from django import forms
from .models import CustomUser


class CustomSignupForm(SignupForm):
    nome = forms.CharField(max_length=255, required=True)
    cognome = forms.CharField(max_length=255, required=True)
    sito_web = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_class = 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': css_class, 'placeholder': field.label})

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Indirizzo email già in uso. Inserisci un indirizzo email diverso.")
        return email


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_class = 'form-control'
        for field_name, field in self.fields.items():
            if field_name == 'remember':
                field.widget.attrs.update(
                    {'class': 'form-check-input', 'placeholder': field.label})
            else:
                field.widget.attrs.update(
                    {'class': css_class, 'placeholder': field.label})

    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_class = 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': css_class, 'placeholder': field.label})


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_class = 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': css_class, 'placeholder': field.label})
