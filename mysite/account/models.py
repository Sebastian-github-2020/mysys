from django.db import models


# Create your models here.

class MyAccount(models.Model):
    account_description = models.CharField(max_length=100,verbose_name='描述')
    account_name = models.CharField(max_length=50,verbose_name='账户名')
    account_password = models.CharField(max_length=50,verbose_name='密码')
    create_date = models.DateTimeField(blank=True, null=True,verbose_name='创建日期')
    modify_date = models.DateTimeField(blank=True, null=True,verbose_name='修改日期')
    email = models.CharField(max_length=100, blank=True, null=True,verbose_name='邮箱')
    phone = models.CharField(max_length=20, blank=True, null=True,verbose_name='手机号')

    class Meta:
        managed = False
        db_table = 'my_account'
