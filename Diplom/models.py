from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
class UserManager(BaseUserManager):
    def create_user(self, email, password, firstname, lastname, phone, position):
        user = self.model(email=self.normalize_email(email), firstname=firstname, lastname=lastname, phone=phone, position=position)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def update_user(self, user_id, email, password, firstname, lastname, phone, position):
        user = User.objects.get(pk=user_id)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.firstname = firstname
        user.lastname = lastname
        user.phone = phone
        user.position = position
        user.save(using=self._db)


class UserType(models.Model):
    type = models.CharField(verbose_name='type', max_length=255, default="")


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=11, default="")
    firstname = models.CharField(verbose_name='firstname', max_length=255, default="")
    lastname = models.CharField(verbose_name='lastname', max_length=255, default="")
    position = models.CharField(verbose_name='position', max_length=255, default="")
    type = models.ForeignKey(UserType, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.firstname
"""


class UserType(models.Model):
    name = models.TextField(verbose_name='name', default="")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(verbose_name='phone', default="")
    user_type = models.ForeignKey(UserType, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Raspberry(models.Model):
    room = models.CharField(verbose_name='room', max_length=255, default="")
    domain = models.CharField(verbose_name='domain', max_length=255, default="")


class Channel(models.Model):
    number = models.IntegerField(verbose_name='number', default=0)
    is_busy = models.BooleanField(verbose_name='is_busy', default=False, db_index=True)
    raspberry = models.ForeignKey(Raspberry, null=True, blank=True)


class DeviceType(models.Model):
    name = models.TextField(verbose_name='name', default="")


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, null=True)
    channel = models.ForeignKey(Channel, null=True)


class DeviceData(models.Model):
    data = models.IntegerField(verbose_name='data', default=0)


class Rule(models.Model):
    user = models.ForeignKey(User, null=True)
    device = models.ForeignKey(Device, null=True)
    time = models.TextField(verbose_name='time', default="")
    mode = models.BooleanField(verbose_name='mode', default=False)
