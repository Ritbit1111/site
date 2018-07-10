
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class TreadersProfile(models.Model):
    trader  = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    id_list = models.CharField(max_length=100, default="None", verbose_name='Account IDs',)

    def __str__(self):
        return self.trader.first_name


def create_profile(sender, **kwargs):
    if kwargs['created']:
        trader_profile = TreadersProfile.objects.create(trader = kwargs['instance'])

post_save.connect(create_profile, sender=User)