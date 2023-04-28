from django.db import models



class ContactUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='پیام')
    read = models.BooleanField(default=False, verbose_name='خوانده شده')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    mail = models.EmailField(max_length=100, verbose_name='ایمیل')
    response = models.TextField(verbose_name='پاسخ', null=True, blank=True)
    def __str__(self):
        return f'{self.title}({self.name})'
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'



class UserProfile(models.Model):
    image = models.ImageField(verbose_name='تصویر', upload_to='images')















