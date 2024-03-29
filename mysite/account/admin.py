from django.contrib import admin
from .models import MyAccount, Movie
from django.utils.safestring import mark_safe


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    # 指定在admin页数据列表显示的字段
    list_display = [
        'id',
        'account_description',
        'account_name',
        'account_password',
        'create_date',
        'modify_date',
        'email',
        'phone'
    ]
    # 添加数据的时候显示的字段
    fields = ['account_description',
              'account_name',
              'account_password',
              'email',
              'phone']
    # 字段比较多的时候 可以给字段分类 和上面的 fields字段 冲突 2选1吧
    # fieldsets = [
    #     ("主要信息", {'fields': ['account_description',
    #                          'account_name',
    #                          'account_password', ]}),
    #     ('联系信息', {'fields': ['email', 'phone']})
    # ]
    search_fields = ('account_name', 'account_description', 'email')


class MovieAdmin(admin.ModelAdmin):
    fields = ['movie_hero_name', 'movie_date', 'movie_film_name', 'movie_img','movie_content']
    list_display = ['movie_hero_name', 'movie_date', 'movie_film_name', 'movie_img', 'movie_img_data']


admin.site.register(MyAccount, AccountAdmin)
admin.site.register(Movie, MovieAdmin)

admin.site.site_header = "账户管理系统"
admin.site.site_title = "账户管理"
admin.site.index_title = "后台首页"
