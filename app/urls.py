from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail),
]