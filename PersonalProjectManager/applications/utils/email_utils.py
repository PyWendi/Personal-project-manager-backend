from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import secrets
from django.core.cache import cache
from django.conf import settings
import logging
logger = logging.getLogger(__name__)

def generate_verification_code():
    """Generate a secure 6-digit verification code."""
    return str(secrets.randbelow(10**6)).zfill(6)


def send_verification_email(to_email):
    """Send a verification email with a code."""
    try:
        code = generate_verification_code()

        subject = "Your Verification Code"
        from_email = settings.EMAIL_HOST_USER
        html_content = render_to_string("emails/verification_email.html", {"code": code})
        text_content = render_to_string("emails/verification_email.txt", {"code": code})

        msg = EmailMultiAlternatives(subject, text_content, from_email, to=[to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        cache.set(f"verify_{to_email}", code, timeout=300) #5 minutes
        print(f"Logging code : {code}")

        return 200, code  # You may want to return it for saving in DB/session
    except Exception as e:
        logger.error(f"Error sending verification email to {to_email}: {e}")
        print(str(e))
        return 500, f"Error sending verification email to {to_email}: {e}"
