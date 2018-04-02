from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

app_name = 'text'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^topics/$', views.IndexView.as_view(), name="index"),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(), name='detail'),
    url(r'album/add/$',views.AlbumCreate.as_view(), name="album-add"),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),
]