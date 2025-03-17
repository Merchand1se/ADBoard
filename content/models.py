from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.urls import reverse
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


class User(AbstractUser):
    code = models.CharField(max_length=10, blank=True, null=True)

class Post(models.Model):
    Tanks = 'Tk'
    Heal = 'Hl'
    DD = 'DD'
    Dealer = 'Dl'
    Gildmasters = 'Gm'
    Questgivers = 'Qg'
    Вlacksmith = 'Bs'
    Skinner = 'Sk'
    Alchemist = 'Ach'
    Wizard_of_spells = 'Wof'
    CATEGORY_CHOICES =[
        (Tanks, 'Tanks'),
        (Heal, 'Heal'),
        (DD, 'DD'),
        (Dealer, 'Dealer'),
        (Gildmasters, 'Gildmasteers'),
        (Questgivers, 'Questgivers'),
        (Вlacksmith, 'Вlacksmith'),
        (Skinner, 'Skinner'),
        (Alchemist, 'Alchemist'),
        (Wizard_of_spells, 'Wizard of spells')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    creationdate = models.DateTimeField(auto_now_add=True, verbose_name='Date time')
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.CharField(max_length=1000, verbose_name='Description')
    category_choice = models.CharField(_('Category choice'), max_length=3,choices=CATEGORY_CHOICES, default=Tanks)
    price = models.IntegerField(max_length=1000000, default=0)
    users = models.ManyToManyField(User, related_name='favorite_posts')
    media = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True, verbose_name='Media')
    #mediaHTML = HTMLField(max_length=10000, verbose_name='Media')


    def _get_absolte_url(self):
        return reverse('', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}cd ')

    def like(self):
        User.favorite_posts.add(Post.object.get(id=1))

    def dislike(self):
        User.favorite_posts.remove(Post.object.get(id=1))

    def preview(self):
        return f'{self.title[:20]}...'



class Reply(models.Model):
    accept = 'accept'
    reject = 'reject'
    ACCEPTION_CHOICES = [(accept, _('Accept')), (reject, _('reject'))]
    post_replied = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post replied')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='Replies', verbose_name='User replied')
    text = models.TextField(verbose_name='Description')
    timecreated = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')
    acception_choice = models.CharField(_('Accept/Reject'), max_length=7,choices=ACCEPTION_CHOICES, default=reject)



    def preview(self):
        return f'{self.text[:123]} ...'

    def get_absolute_url(self):
        return reverse('ReplyDetail', args=[str(self.id)])

