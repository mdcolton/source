from django.conf.urls import url
from groups import views

urlpatterns = [
    url(r'^groups/$', views.group_list),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.group_detail),
]