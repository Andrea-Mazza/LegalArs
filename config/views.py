from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from . import forms
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from userArea.models import CustomUser
from blog.models import Articolo
from django.db.models import Q
from recuperoCredito.models import ServizioRecuperoCredito


# Create your views here

# def base(request):
#     user = CustomUser.objects.get(pk=request.user.pk)
#     recupero_credito = ServizioRecuperoCredito.objects.filter(
#         current_user=user)
#     avvisi = False
#     context = {'recupero': recupero_credito}
#     if recupero_credito.filter(comunicazioni_non_lette__gt=0).exists():
#         avvisi = True
#     else:
#         avvisi = False
#     context['avvisi'] = avvisi
#     return render(request, 'base.html', context)

def error_404(request, exception):
    return render(request, '404.html', status=404)


def redirectEstia(request):
    return redirect('estiaPartner')


def redirectPressArea(request):
    return redirect('blog-news')


def redirect_blog_article(request, slug):
    return redirect('blog_news_details', slug=slug)


def redirectFonti(request):
    return redirect('blog-fonti')


def redirectFontiDetails(request, slug):
    return redirect('blog_fonti_details', slug=slug)


def redirectChiSiamo(request):
    return redirect('chiSiamo')


def redirectCivile(request):
    return redirect('diritto-civile')


def redirectPenale(request):
    return redirect('diritto-penale')


def redirectAmministrativo(request):
    return redirect('diritto-amministrativo')


def redirectLavoro(request):
    return redirect('diritto-lavoro')


def redirectInvestimenti(request):
    return redirect('truffe-online')


def redirectDivorzi(request):
    return redirect('separazioni-divorzi')


def redirectEsdebitazione(request):
    return redirect('esdebitazione')


def redirectAmbiente(request):
    return redirect('reati-ambientali')


def redirectMandato(request):
    return redirect('mandato-europeo')


def redirectEstate(request):
    return redirect('real-estate')


def redirectDiffamazione(request):
    return redirect('diffamazione')


def redirectMedica(request):
    return redirect('colpa-medica')


def redirectBanca(request):
    return redirect('rapporti-bancari')


def redirectImmagine(request):
    return redirect('tutela-immagine')


def redirectImpresa(request):
    return redirect('diritto-impresa')


def redirectSoggiorno(request):
    return redirect('permesso-soggiorno')


def redirectRisanamento(request):
    return redirect('impresa-risanamento')


def redirectEsattoriali(request):
    return redirect('atti-esattoriali')


def home(request):
    posts = Articolo.objects.all()[:9]
    context = {'posts': posts}
    return render(request, 'home.html', context)


def privacyPage(request):
    return render(request, 'privacy.html')


def legalSharing(request):
    return render(request, 'legal_sharing.html')


def estiaPartner(request):
    return render(request, 'estia.html')


def chiSiamo(request):
    return render(request, 'chi_siamo.html')


def dirittoCivile(request):
    return render(request, 'diritto_civile.html')


def dirittoPenale(request):
    return render(request, 'diritto_penale.html')


def dirittoAmm(request):
    return render(request, 'diritto_amm.html')


def dirittoLavoro(request):
    return render(request, 'diritto_lavoro.html')


def truffeOnline(request):
    return render(request, 'investimenti_e_truffe.html')


def divorzi(request):
    return render(request, 'divorzi.html')


def esdebitazione(request):
    return render(request, 'esdebitazione.html')


def reatiAmbientali(request):
    return render(request, 'reati_ambientali.html')


def mandatoUe(request):
    return render(request, 'mandato_europeo.html')


def realEstate(request):
    return render(request, 'real_estate.html')


def diffamazione(request):
    return render(request, 'diffamazione.html')


def colpaMedica(request):
    return render(request, 'colpa_medica.html')


def rapportiBancari(request):
    return render(request, 'rapporti_bancari.html')


def tutelaImmagine(request):
    return render(request, 'tutela_immagine.html')


def dirittoImpresa(request):
    return render(request, 'diritto_impresa.html')


def permessoSoggiorno(request):
    return render(request, 'permesso_soggiorno.html')


def impresaRisanamento(request):
    return render(request, 'impresa_risanamento.html')


def attiEsattoriali(request):
    return render(request, 'atti_esattoriali.html')


def contatti(request):
    return render(request, 'contatti.html')


def ricerca(request):
    form = forms.RicercaArticoloForm()
    query = None
    results = []

    if 'ricerca' in request.GET:
        form = forms.RicercaArticoloForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['ricerca']
            results = Articolo.objects.filter(Q(
                titolo__icontains=query) | Q(corpo__icontains=query)).distinct()

    context = {
        'form': form,
        'query': query,
        'results': results
    }
    return render(request, 'ricerca.html', context)


def signup(request):
    registration_form = RegisterForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            registration_form = RegisterForm(request.POST)
            if registration_form.is_valid():
                name = registration_form.cleaned_data.get('name')
                surname = registration_form.cleaned_data.get('surname')
                email = registration_form.cleaned_data.get('email')
                password = registration_form.cleaned_data.get('password1')
                user = CustomUser.objects.create_user(
                    email=email, name=name, surname=surname, password=password)
                auth_login(request, user)
                return redirect('userArea:user_home')
    return render(request, 'signup.html', {'registration_form': registration_form})


def login(request):
    login_form = LoginForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=email, password=password)
                auth_login(request, user)
                return redirect('userArea:user_home')
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('accesso')


class password_reset(PasswordResetView):
    template_name = 'password_reset_form.html'
    form_class = forms.CustomPasswordResetForm
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    # def form_valid(self, form):
    #     UserModel = get_user_model()
    #     email = form.cleaned_data['email']
    #     if UserModel.objects.filter(email=email).exists():
    #         # The email exists in the database, proceed with sending the password reset email
    #         # You can use the default code to send the email here
    #         # Send the email with a password reset link
    #         user = form.get_user()
    #         token = default_token_generator.make_token(user)
    #         url = reverse('password_reset_confirm', kwargs={
    #                       'uidb64': user.id, 'token': token})
    #         reset_url = f"{self.request.scheme}://{self.request.META['HTTP_HOST']}{url}"
    #         send_mail(
    #             'Password reset for your account',
    #             f'Use this link to reset your password: {reset_url}',
    #             'mazzaandrea45@gmail.com',
    #             [email],
    #             fail_silently=False,
    #         )
    #         return super().form_valid(form)
    #     else:
    #         # The email does not exist in the database, show an error message to the user
    #         form.add_error(
    #             'email', 'This email address does not exist in our database.')
    #         return self.form_invalid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = forms.CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.POST)
        return context

    def form_valid(self, form):
        # Reset the user's password
        form.save()
        return super().form_valid(form)


class CustomPasswordResetCompleteView(TemplateView):
    template_name = 'password_reset_complete.html'
