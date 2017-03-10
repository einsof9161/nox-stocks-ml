from django.conf.urls import url

from . import views

urlpatterns = [
    
    # ex: /stock/
    url(r'^$', views.list, name='list'),
    # ex: /stock/2391/
    url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
    
]