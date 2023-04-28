from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models



class User(AbstractUser):
    avatar = models.ImageField(verbose_name='تصویر کاربر', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی با ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()