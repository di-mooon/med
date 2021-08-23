import smtplib
from email.mime.multipart import MIMEMultipart
from platform import python_version
from email.mime.text import MIMEText
import string
import random

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from user.models import UserToken


def send_mail_smpt(recipients, text):
    server = 'smtp.yandex.ru'
    user = 'confirmemaildjango@yandex.ru'
    password = 'confirmemaildjango1234'
    subject = 'Подтверждение электронной почты'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Registration <' + user + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = user
    msg['Return-Path'] = user
    msg['X-Mailer'] = 'Python/' + (python_version())
    part_text = MIMEText(f"Вы успешно зарегистрировались.\n"
                         f"Для активации аккаунта перейдите по ссылке:  http://127.0.0.1:8000/profile/activate/{text}/\n "
                         f"Если данное письмо отправлено Вам ошибочно, проигнорируйте его.", 'plain')
    msg.attach(part_text)
    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(user, recipients, msg.as_string())
    mail.quit()


def profile_activate(email):
    user, created = UserToken.objects.get_or_create(email=email)
    if user.token:
        send_mail_smpt(email, user.token)
    else:
        user.token = PasswordResetTokenGenerator()
        user.save()
        send_mail_smpt(email, user.token)
