from django.conf.urls import url
from . import views

urlpatterns = (
    # 授权
    url(r'', views.index , name='index'),

    # 获取用户信息
    url(r'^info/$', views.get_info, name='get_info'),
)
