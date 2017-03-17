from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='tes1t'),
    url(r'^login/', views.test, name='test'),
    url(r'^signup/', views.test, name='test2'),
    url(r'^question/(\d+)/$', views.test, name='test3'),
    url(r'^ask/', views.test, name='test4'),
    url(r'^popular/', views.test, name='test5'),
    url(r'^new/', views.test, name='test6')
]