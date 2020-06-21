from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login"),
    url(r'^questions/$', views.questions, name="questions"),
]