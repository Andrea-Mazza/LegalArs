from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from userArea.models import CustomUser
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation


class AssistenzaUserArea(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    messaggio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Messaggio', 'id': 'messaggio'}))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    def get_user(self):
        UserModel = get_user_model()
        email = self.cleaned_data.get('email')
        if email:
            try:
                return UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                pass
        return None


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome', 'id': 'nome'}))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Cognome', 'id': 'cognome'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Indirizzo email', 'id': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Conferma password', 'id': 'password2'}))

    def clean_username(self):
        super().clean()
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError(
                "Questo campo deve contenere un minimo di 4 caratteri. Correggi per favore.")
        elif len(username) < 1:
            raise forms.ValidationError(
                "Questo campo è obbligatori per la creazione di un account. Per favore inserisci un minimo di 4 caratteri per procedere alla registrazione del tuo account")
        elif CustomUser.objects.filter(username=username).exists():
            i = 1
            new_username = f"{username}_{i}"
            while CustomUser.objects.filter(username=new_username).exists():
                i += 1
                new_username = f"{username}_{i}"
                suggestion = f"{new_username}"
                raise forms.ValidationError(
                    f"Sembra che questo username sia già stato già registrato da qualcun'altro. Ecco alcuni suggerimenti {suggestion}")
            # return new_username
        return username

    def clean_email(self):
        super().clean()
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Un utente con questa email esiste già. Sei tu? Allora accedi utlizzando questo indirizzo nel form di accesso.")
        try:
            validate_email(email)
        except:
            raise forms.ValidationError(
                "L'indirizzo da te inserito non sembra essere valido. Assicurati che segua il formato standard di ogni email: esempio@gmail.com")

        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        validate_password(password)
        return password

    def clean_password2(self):
        super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Le password inserite risultano diverse. Sii sicuro di inserire la stessa password in entrambi i campi.")
        return password2

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        username = self.cleaned_data.get('username')
        user = CustomUser.objects.create_user(
            email=email, password=password, username=username)
        user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}))

    # def clean_username(self):
    #     super().clean()
    #     username = self.cleaned_data.get('username')
    #     if len(username) < 1:
    #         raise forms.ValidationError(
    #             'Questo campo è obbligatorio, assicurati di aver inserito gli stessi dati inseriti al momento della registrazione. Ti ricordiamo che questo campo deve contenere un minimo di 4 caratteri.')
    #     elif not User.objects.filter(username=username).exist():
    #         raise forms.ValidationError(
    #             'Il nome da te inserito non risulta essere presente tra i nostri iscritti. Assicurati di aver inserito lo stesso testo inserito al momento della registrazione oppure registrati con il form qui sotto.')
    #     return username

    # def clean_email(self):
    #     super().clean()
    #     email = self.cleaned_data.get('email')
    #     try:
    #         validate_email(email)
    #     except:
    #         raise forms.ValidationError(
    #             "L'indirizzo da te inserito non sembra essere valido. Assicurati che segua il formato standard di ogni email: esempio@gmail.com")
    #     if not User.object.filter(email=email):
    #         raise forms.ValidationError(
    #             "L'indirizzo da te inserito non risulta essere associato a nessun utente registrato. Sei sicuro di aver inserito tutti i caratteri correttamente o di non aver dimenticato di inserirne alcuni? Ricorda che, se non sei registrato, puoi utilizzare il form qui sotto.")
    #     return email

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=username, email=email, password=password)
    #     if len(username) < 4:
    #         raise forms.ValidationError(
    #             'Questo campo deve contenere almeno 4 caratteri per essere valido')
    #     elif not User.objects.filter(username).exist():
    #         raise forms.ValidationError(
    #             "L'username da te inserito non risulta associato a nessun utente registrato. Assicurati di aver scritto correttamente l'username che hai usato al momento della registrazione.")

    #     try:
    #         validate_email(email)
    #     except:
    #         raise forms.ValidationError(
    #             "L'indirizzo da te inserito non sembra essere valido. Assicurati che segua il formato standard di ogni email: esempio@gmail.com")

    #     if user is None:
    #         raise forms.ValidationError(
    #             "Le credenziali da te inserite non sono corrette. Assicurati di aver inserito gli stessi dati che hai usato al momento della registrazione.")

    #     return self.cleaned_data
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get("password")

    #     if len(username) < 4:
    #         raise forms.ValidationError(
    #             "Questo campo deve contenere un minimo di 4 caratteri per essere valido.")

    #     if username is not None and password:
    #         self.user_cache = authenticate(
    #             self.request, username=username, email=email, password=password
    #         )
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)

    #     return self.cleaned_data

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class EmailToResetPass(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Indirizzo email'}))


class CustomSetPasswordForm(SetPasswordForm):
    # Definizione dei campi new_password1 e new_password2
    new_password1 = forms.CharField(
        label=_("New password"),  # Etichetta del campo
        # Widget personalizzato con attributo CSS "class"="form-control"
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,  # Non rimuove gli spazi bianchi iniziali e finali
        help_text=password_validation.password_validators_help_text_html(),  # Testo di aiuto
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),  # Etichetta del campo
        strip=False,  # Non rimuove gli spazi bianchi iniziali e finali
        # Widget personalizzato con attributo CSS "class"="form-control"
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class RicercaArticoloForm(forms.Form):
    ricerca = forms.CharField(label='Ricerca', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ricerca'}), help_text="Inserisci una sequenza di lettere per iniziare una ricerca tra gli articoli presenti su LegalArs.")
