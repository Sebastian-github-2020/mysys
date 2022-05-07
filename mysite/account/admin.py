from django.contrib import admin
from .models import MyAccount


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
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


admin.site.register(MyAccount, AccountAdmin)
