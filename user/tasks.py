from config.celery import app
from .service import send_mail_activate_account


@app.task
def send_activate_account(subject, body, email):
    send_mail_activate_account(subject, body, email)
