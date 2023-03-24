from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect 


def send_account_activation_email(email , email_token):
    subject = 'Your accounts needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    print("about to send email")
    send_email(subject , message , email_from , [email])


def send_email(subject , message , email_from , email):
    print(message)
    print(email)
    msg = EmailMessage("activation link",message, to=email)
    msg.send()

    return HttpResponseRedirect('/')