from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reply, Post, User
from django.core.mail import send_mail

#Logining email signal
@receiver(post_save, sender=User)
def login_email_sending(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Welcome to Advertisement Board!',
            message=f'Hey, {instance.username}! We are really glad that you have visited or AD. Board',
            from_email='mevmavmva@gmail.com',
            recipient_list=[instance.email],
        )

@receiver(post_save, sender=Reply)
def reply_email_sending(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'Hey {instance.post_replied.author.username} you have a new announcement response {instance.post_replied.title}',
            message=f'User {instance.user.username} replied on your advertisement',
            from_email='mevmavmva@gmail.com',
            recipient_list=[instance.post_replied.author.email]
        )


