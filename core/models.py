from django.db import models
from django.contrib.auth.models import AbstractUser


class CompetitionUser(AbstractUser):
    surname = models.CharField(max_length=250, verbose_name='Отчество', blank=True, null=True)




