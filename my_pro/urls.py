"""my_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from urllib import request
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('add',views.add),
    path('login',views.login),
    path('uregister',views.uregister),
    path('creg',views.creg),
    path('cview',views.cview),
    path('cfview',views.cfview),
    path('rfview',views.rfview),
    path('ulogin',views.ulogin),
    path('ulogout',views.ulogout),
    path('vprofile',views.vprofile),
    path('adminview',views.adminview),
    path('cdelete/<int:id>',views.cdelete,name="cdelete"),
    path('udelete/<int:id>',views.udelete,name="udelete"),
    path('cupdate/<int:id>',views.cupdate,name="cupdate"),
    path('cupdate/ccupdate/<int:id>',views.ccupdate,name="ccupdate"),
    path('uupdate/<int:id>',views.uupdate,name="uupdate"),
    path('uupdate/uuupdate/<int:id>',views.uuupdate,name="uuupdate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
