from django.urls import path
from .views import accounts
from .drfViews import *
from rest_framework.routers import DefaultRouter

# from rest_framework.urls import

router = DefaultRouter()
router.register("api", MyAccountView)
router.register("api1", MyAccountModelViewSet, basename="login")

app_name = 'account'
urlpatterns = [
                  path('index', accounts, name='index'),  # 查询账户
                  path("drfapi", MyAccountAPIView.as_view()),
                  path("apiview/<int:account_id>", MyAccountInfoAPIView.as_view()),
                  path("gview/<int:id>", MyAccountInfoGenericView.as_view()),
                  path("glview/", MyAccountListMixinView.as_view()),
                  path("grview/<int:pk>", MyAccountMixinView.as_view()),
                  path("glaview", MyAccountListApiView.as_view()),
              ] + router.urls
