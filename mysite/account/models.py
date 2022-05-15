from django.db import models


# Create your models here.

class MyAccount(models.Model):
    """账户管理模型"""
    account_description = models.CharField(max_length=100, verbose_name='描述')
    account_name = models.CharField(max_length=50, verbose_name='账户名')
    account_password = models.CharField(max_length=50, verbose_name='密码')
    create_date = models.DateTimeField(blank=True, null=True, verbose_name='创建日期')
    modify_date = models.DateTimeField(blank=True, null=True, verbose_name='修改日期')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='邮箱')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='手机号')

    class Meta:
        managed = False
        db_table = 'my_account'


class Movie(models.Model):
    """影片管理模型"""
    movie_hero_name = models.CharField(max_length=100, verbose_name="演员名称")
    movie_date = models.DateField(verbose_name="发布日期")
    movie_film_name = models.CharField(max_length=100, verbose_name="影片名称")
    movie_img = models.CharField(max_length=200, verbose_name='图片路径')
