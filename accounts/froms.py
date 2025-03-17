from allauth.account.forms import SignupForm
from content.models import User
from django.core.mail import send_mail
from string import hexdigits
from django.conf import settings
import random

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        #common_users = Group.objects.get(name='common users')
        #user.groups.add(common_users)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject='This is your activation code',
            message=f'Hey, {user.username}! There is your {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user
