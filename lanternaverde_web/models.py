from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.db import models
from django.utils import timezone
import re

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser,
                     **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',
                                max_length=20,
                                unique=True,
                                help_text="Required. 15 characters or fewer." +
                                "Letters, numbers and @/./+/-/_ characters",
                                validators=[
                                    validators.RegexValidator(
                                        re.compile(r'^[\w.@+-]+$'),
                                        'Enter a valid username.', 'invalid')])

    first_name = models.CharField('Nome', max_length=35)
    last_name = models.CharField('Sobrenome', max_length=30)
    email = models.EmailField('Endereço de email', max_length=255, unique=True)

    is_staff = models.BooleanField('staff status', default=False, help_text=
        'Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True, help_text=
        'Designates whether this user should be treated as active. ' + 
        'Unselect this instead of deleting accounts.')

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Analista(models.Model):
    available = models.BooleanField('Disponivel', default=True)
    cpf = models.CharField('CPF', max_length=11)
    specialty = models.CharField('Especialidade', max_length=255)

    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'analista'
        verbose_name_plural = 'analistas'


