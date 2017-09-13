from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index,  name = 'index'),
	url(r'^members/([a-zA-Z0-9-]+)/$', views.detail ,name = 'detail'),
	url(r'^members/([a-zA-Z0-9-]+)/edit', views.edit ,name = 'edit'),
]