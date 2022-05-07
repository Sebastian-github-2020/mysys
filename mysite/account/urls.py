from django.urls import path
from .views import accounts

app_name = 'account'
urlpatterns = [
    path('index/<str:search_key>', accounts, name='index'), # 查询账户
]
