from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    def get_short_name(self):
        return self.nick_name

    def get_full_name(self):
        return self.nick_name

    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', choices=(('male', '男'), ('female', '女')), default='female', max_length=10)
    address = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.jpg', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField('类型', choices=(('register', '注册'), ('forget', '忘记密码')), max_length=20)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Banner(models.Model):
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m')
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
