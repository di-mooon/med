from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from djangoProject1.settings import EMAIL_HOST_USER
from user.models import Mail_Domains


def profile_activate(request, user):
    email = request.POST.get('email')
    site = get_current_site(request)
    message = render_to_string('send_mail/activate_account_email.html', {
        'email': email,
        'user': user,
        'protocol': 'http',
        'domain': site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    message = ''.join(message.splitlines())
    email_message = EmailMultiAlternatives(
        'Подтверждение электронной почты',
        message,
        EMAIL_HOST_USER,
        [email]
    )
    email_message.send()
