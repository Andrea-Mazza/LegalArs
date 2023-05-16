from .forms import AssistenzaForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage


def CustomContext(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        if request.method == 'POST':
            assistenza_form = AssistenzaForm(
                {'email': f'{user.email}'}, request.POST)
            if assistenza_form.is_valid():
                email = assistenza_form.cleaned_data['email']
                messaggio = assistenza_form.cleaned_data['messaggio']

                email_to_owner = EmailMessage(
                    'Richiesta di assistenza',
                    f"Un utente, la cui email è {email}, ha richiesto assistenza dalla sua area personale.\nL'utente ha inviato il seguente messaggio:\n {messaggio}",
                    'mazzaandrea45@gmail.com',  # mittente
                    ['mazzaandrea45@gmail.com',],  # destinatario
                )

                email_to_client = EmailMessage(
                    'Richiesta ricevuta',
                    f"Abbiamo appena ricevuto la tua richiesta di assistenza e abbiamo anche ricevuto il tuo messaggio. Ti contatteremo nel minor tempo possibile.\nNell'attesa vogliamo augurarti un buon proseguimento di giornata.\nIl team di LegalArs",
                    'mazzaandrea45@gmail.com',  # mittente
                    [f'{email}',],  # destinatario
                )

                try:
                    email_to_owner.send()
                    email_to_client.send()
                except BadHeaderError:
                    return print('Ops qualcosa è andato storto')

        else:
            assistenza_form = AssistenzaForm({'email': f'{user.email}'})

        context = {'assistenza_form': assistenza_form, 'user': user}
    return context
