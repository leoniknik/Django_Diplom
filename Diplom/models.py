from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password, firstname, lastname, phone):
        if email and password and firstname and lastname and phone:
            user = self.model(email=self.normalize_email(email), firstname=firstname, lastname=lastname, phone=phone)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def update_user(self, user_id, email, password, firstname, lastname, phone):
        user = User.objects.get(pk=user_id)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.firstname = firstname
        user.lastname = lastname
        user.phone = phone
        user.save(using=self._db)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=11, default="")
    firstname = models.CharField(verbose_name='firstname', max_length=255, default="")
    lastname = models.CharField(verbose_name='lastname', max_length=255, default="")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstname + self.lastname

    def get_short_name(self):
        return self.firstname
