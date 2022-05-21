from django.db import models
from django.utils.html import format_html


# Create your models here.

class MyAccount(models.Model):
    """账户管理模型"""
    account_description = models.CharField(max_length=100, verbose_name='描述')
    account_name = models.CharField(max_length=50, verbose_name='账户名')
    account_password = models.CharField(max_length=50, verbose_name='密码')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    modify_date = models.DateTimeField(verbose_name='修改日期', auto_now=True)
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='邮箱')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='手机号')

    class Meta:
        verbose_name = "账户"
        verbose_name_plural = "账户"
        managed = False
        db_table = 'my_account'


class Movie(models.Model):
    """影片管理模型"""
    movie_hero_name = models.CharField(max_length=100, verbose_name="演员名称", null=False)
    movie_date = models.DateField(verbose_name="发布日期")
    movie_film_name = models.CharField(max_length=100, verbose_name="影片名称", null=False)
    movie_img = models.ImageField(verbose_name='图片路径', null=False, upload_to="account")
    movie_evaluate = models.CharField(max_length=200, verbose_name="评价", default="没有添加评价")

    def movie_img_data(self):
        print(self.movie_img)
        if self.movie_img:
            return format_html('<img src="/media/{}" width="100px"/>', self.movie_img)
        else:
            return format_html('<p>没有图片</p>')

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = "电影"
