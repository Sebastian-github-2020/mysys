from django.urls import path
from .views import accounts
from .drfViews import MyAccountView, MyAccountAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api", MyAccountView)
app_name = 'account'
urlpatterns = [
                  path('index', accounts, name='index'),  # 查询账户
                  path("drfapi", MyAccountAPIView.as_view())
              ] + router.urls
