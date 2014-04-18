from django.core.mail import send_mail


def send_key_email(email, message):
        email_subject = "KHAS Help Desk"
        email_body = message
        from_mail = "muratcanumit@gmail.com"
        send_mail(email_subject, email_body,
                  from_mail, [email, ], fail_silently=False)
